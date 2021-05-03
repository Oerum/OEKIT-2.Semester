import mysql.connector
from flask import *
import numpy as np

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

    #header
    header = ["Total Sum of Sales"]

    #Nested loop to remove irrelevant decimals and symbols#
    sum = []
    for v in myresult:
      for t in v:
        sum.append(t)


    return render_template('tabel_løb.html', header=header, datasæt=sum)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Home') == 'Home':
            return redirect(url_for('root'))

        elif request.form.get('Total sum') == 'Total sum':
            return redirect(url_for('total_amount'))

        elif  request.form.get('action3') == 'Zealand':
            return redirect(url_for('zealand'))


    return render_template("tabel_løb.html")


if __name__ == '__name__':
  app.run(debug=True)
app.run(port=5000)

