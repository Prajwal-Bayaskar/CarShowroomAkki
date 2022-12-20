#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req=cgi.FieldStorage()

nm=req.getvalue("modnm")
newp=int(req.getvalue("newp"))

con=pymysql.connect(host='localhost',user='root',password='root',database='akki')
curs=con.cursor()

try:
   curs.execute("UPDATE Cars  SET price=%d where modnm='%s'"%(newp,nm))
   con.commit()

   print("<h3 style='color:green'>Price Updation was successfull..!</h3>")
except Exception as e:
   print(e)
   print("<h3 style='color:red'>Price Updation failed !</h3>")

   con.close()