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


out_stream = xlsx2html('/Users/filiporum-petersen/Downloads/Gantt-kort.xlsx')
out_stream.seek(0)
print(out_stream.read())





