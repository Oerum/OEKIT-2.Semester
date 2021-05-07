import mysql.connector
from flask import *
import numpy as np
from xlsx2html import xlsx2html

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



sql = "SELECT ProductId, Name ,profitrate FROM produkter"
mycursor.execute(sql)
myresult = mycursor.fetchall()

id = []
name = []
profit = []
for p, n, r in myresult:
  id.append(p)
  name.append(n)
  profit.append(r)

for i in id:
  print(i)






