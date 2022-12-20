#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req=cgi.FieldStorage()
typ=req.getvalue("cartype")

con=pymysql.connect(host='localhost',user='root',password='root',database='akki')
curs=con.cursor()

curs.execute("select * from cars where cartype='%s'"%typ)
con.commit()
data=curs.fetchall()

print(data)