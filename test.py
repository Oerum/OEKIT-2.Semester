import mysql.connector
from flask import *
import numpy as np
from xlsx2html import xlsx2html
import random
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


sql = "SELECT indkøbsordre.Productid, Date, name, Freightno, amount, produkter.PurchasePrice, amount*produkter.PurchasePrice FROM indkøbsordre, produkter Where indkøbsordre.ProductId = produkter.ProductId ORDER BY indkøbsordre.ProductId DESC;"

mycursor.execute(sql)
myresult = mycursor.fetchall()

productid = []
date = []
name = []
freightno = []
amount = []
purchaseprice = []
summ = []
for i,d,n,f,a,p,s in myresult:
  productid.append(i)
  date.append(d)
  name.append(n)
  freightno.append(f)
  amount.append(a)
  purchaseprice.append(p)
  summ.append(s)

total_sum = ("{:,}".format(np.sum(summ)))
total_sum_cal = sum(summ)

sql = "SELECT sum(Quantity*UnitPrice) FROM salgsordre"
mycursor.execute(sql)
myresult = mycursor.fetchall()

sum_sales = []
sum_sales_cal = []
for v in myresult:
  for t in v:
    sum_sales.append("{:,}".format(t))
    sum_sales_cal.append(t)

total_rev = (sum_sales_cal[0]-total_sum_cal)

