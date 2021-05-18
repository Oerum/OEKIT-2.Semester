import mysql.connector
from flask import *
import numpy as np

try:
  mydb = mysql.connector.connect(
    host="localhost", #boundsoul19375.ddns.net # Change settings to suit your preference
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
try:
  app = Flask(__name__)

  @app.route('/')
  def root():
    return redirect(url_for('home'))

  @app.route('/home')
  def home():
    return render_template('home.html')

  @app.route('/generelt')
  def generel():
      sql = "SELECT sum(Quantity*RetailPrice) FROM salgsordre"
      mycursor.execute(sql)
      myresult = mycursor.fetchall()

      #header#
      header = ["Total salg"]
      #Nested loop to remove irrelevant decimals and symbols#
      sum = []
      for v in myresult:
        for t in v:
          sum.append("{:,}".format(t))
      #Total_Sales for each element
      sql = "SELECT OrderDate, sum(Quantity*RetailPrice) FROM salgsordre GROUP BY  OrderDate"
      mycursor.execute(sql)
      myresult = mycursor.fetchall()

      sales_clean = []
      dates_d = []
      sales_d = []
      for d, s in myresult:
          dates_d.append(str(d))
          sales_d.append("{:,}".format(s))
          sales_clean.append(int(s))

      return render_template('generelt.html', header=header, datasæt=sum, date=dates_d, sales_clean=sales_clean, sales_date=zip(dates_d,sales_d))

  @app.route('/erhvervsøkonomi')
  def erhversøkonomi():
      #Find ProfitRate for each product
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
      #Find postalcode and city to determine which area purchases most
      sql = "SELECT postnr, COUNT(city) FROM kunder group BY postnr ORDER by postnr "
      mycursor.execute(sql)
      myresult = mycursor.fetchall()

      post = []
      city = []

      for p, c in myresult:
        post.append(p)
        city.append(c)


      return render_template('erhvervsøkonomi.html', id_name_profit=zip(id, name, profit), city=city, post=post, post_sale=zip(post,city))



  @app.route('/projektledelse') #Takes a while to load page due to onedrive embedding#
  def projektledelse():
    return render_template('projektledelse.html',)


  @app.route('/makroøkonomi')
  def makroøkonomi():
    return render_template('makroøkonomi.html')


  @app.route('/supplychain')
  def Supply_Chain():

    sql = "SELECT indkøbsordre.Productid, Date, name, Freightno, amount, produkter.PurchasePrice, amount*produkter.PurchasePrice FROM indkøbsordre, produkter Where indkøbsordre.ProductId = produkter.ProductId ORDER BY Date DESC;"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    #Data for front-end table#
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

    #Formatting & Calculation for paragraf#
    total_sum = ("{:,}".format(np.sum(summ))) #Purchase
    total_sum_cal = sum(summ) #Purchase_noformat

    sql = "SELECT sum(Quantity*RetailPrice) FROM salgsordre"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    sum_sales = [] #Sales
    sum_sales_cal = [] #Sales_noformat
    for v in myresult:
      for t in v:
        sum_sales.append("{:,}".format(t))
        sum_sales_cal.append(t)

    total_rev = ("{:,}".format((sum_sales_cal[0]-total_sum_cal))) #Calculation of Purchase&Sales_noformat & formatting to be easily readable

    return render_template('supplychain.html', data=zip(productid,date,name,freightno,amount,purchaseprice,summ), total_sum=total_sum,sum_sales=sum_sales, total_rev=total_rev)


  @app.route('/systemudvikling')
  def Systemudvikling():
      return render_template('systemudvikling.html')


  @app.errorhandler(404)
  def page_not_found(error):
      return render_template('home.html'), 404


  if __name__ == '__main__':
      app.run(debug=True)# host="192.168.0.44", port=5000)#Change this to suit your localhost or server#

except:
  print('An error occoured in the backend')
