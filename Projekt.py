import mysql.connector
from flask import *
import numpy as np
import json

try:
  mydb = mysql.connector.connect(
    host="boundsoul19375.ddns.net",
    port=19375,
    user="Filip",
    password="test1234",
    database = "proshop_data"
  )
  mycursor = mydb.cursor()
  #print(f"You are successfully connected to the database: {mydb.database}")

except mysql.connector.errors.ProgrammingError:
  print(f"Error connecting, check credentials")


#Flask GUI
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('home.html')

@app.route('/total')
def total_amount():
    sql = "SELECT sum(Quantity*UnitPrice) FROM salgsordre"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    #header#
    header = ["Total Sum of Sales"]

    #Nested loop to remove irrelevant decimals and symbols#
    sum = []
    for v in myresult:
      for t in v:
        sum.append(t)


    #Total_Sales for each element
    sql = "SELECT OrderDate, sum(Quantity*UnitPrice) FROM salgsordre GROUP BY  OrderDate"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    dates_d = []
    sales_d = []
    for d, s in myresult:
        dates_d.append(str(d))
        sales_d.append(float(s))


    return render_template('tabel_løb.html', header=header, datasæt=sum, dates=json.dumps(dates_d))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host = "192.168.0.44", port = 5000)


