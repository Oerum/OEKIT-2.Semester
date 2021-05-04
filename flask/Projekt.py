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
  return redirect(url_for('home'))

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/generelt')
def generel():
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
        sales_d.append(int(s))

    return render_template('generelt.html', header=header, datasæt=sum, date=dates_d, sales=sales_d)

@app.route('/erhvervsøkonomi')
def erhversøkonomi():
  return render_template('erhvervsøkonomi.html')

@app.route('/projektledelse')
def projektledelse():
  return render_template('projektledelse.html')


@app.route('/makroøkonomi')
def makroøkonomi():
  return render_template('makroøkonomi.html')


@app.route('/supplychain')
def Supply_Chain():
  return render_template('supplychain.html')

@app.route('/systemudvikling')
def Systemudvikling():
  return render_template('systemudvikling.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home.html'), 404


app.static_folder = 'static'
if __name__ == '__main__':
    app.run(debug=True, host = "192.168.0.44", port = 5000) #Change this to suit your localhost or server#


