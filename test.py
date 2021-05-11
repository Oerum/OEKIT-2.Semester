import mysql.connector
from flask import *
import numpy as np
from xlsx2html import xlsx2html
import random
import numpy as np



try:
  mydb = mysql.connector.connect(
    host="localhost",
    port=19375,
    user="Filip",
    password="test1234",
    database = "proshop_data"
  )
  mycursor = mydb.cursor()
  #print(f"You are successfully connected to the database: {mydb.database}")

except mysql.connector.errors.ProgrammingError:
  print(f"Error connecting, check credentials")


sql = "SELECT sum(Quantity*UnitPrice) FROM salgsordre"
mycursor.execute(sql)
myresult = mycursor.fetchall()

#header#
header = ["Total Sum of Sales"]
#Nested loop to remove irrelevant decimals and symbols#
sum = []
for v in myresult:
  for t in v:
    sum.append("{:,}".format(t))
#Total_Sales for each element
sql = "SELECT OrderDate, sum(Quantity*UnitPrice) FROM salgsordre GROUP BY  OrderDate"
mycursor.execute(sql)
myresult = mycursor.fetchall()

sales_clean = []
dates_d = []
sales_d = []
for d, s in myresult:
    dates_d.append(str(d))
    sales_d.append("{:,}".format(s))
    sales_clean.append(int(s))

print(sales_clean)