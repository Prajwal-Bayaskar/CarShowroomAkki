#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type=text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req=cgi.FieldStorage()
nm=req.getvalue("custnm")
mob=req.getvalue("mob")
newmob=req.getvalue("newmob")

con=pymysql.connect(host="localhost",user="root",password="root",database="akki")
curs=con.cursor()

curs.execute("select * from customers update mob='%s' where custnm='%s'"%(newmob,nm))
con.commit()
data=curs.fetchone()

if data:
    print("New mobile number Updated Successfully.....")

else:
    print("<h3><b>Mobile Updation was Unsuccessfull<b><h3>")
con.close()
