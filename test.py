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


sql = "SELECT OrderDate, sum(Quantity*UnitPrice) FROM salgsordre GROUP BY  OrderDate"
mycursor.execute(sql)
myresult = mycursor.fetchall()

dates = []
sales_d = []
for d, s in myresult:
    dates.append(d)
    sales_d.append(float(s))

print(sales_d)

