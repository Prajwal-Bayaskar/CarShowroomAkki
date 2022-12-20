#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req = cgi.FieldStorage()
nm = req.getvalue("custid")

con = pymysql.connect(host="localhost",user="root",password="root",database="akki")
curs = con.cursor()

curs.execute("select * from customers where custid='%s'" % nm)
data = curs.fetchone()
con.commit()


print("<div class='container'><br>")
print("<h3 style='color:blue'>Search Result </h3>")

if data:
    print("<b>Customer Name: ", data[1])
    print("<br>Car : ", data[2])
    print("<br>Amount Paid : ", data[3])
    print("<br>Address : ", data[4])
    print("<br>Mobile : ", data[5])
  

else:
    print("<span style='color:red;font=weight:bold'>")
    print("Customer not found ...")
    print("</span>")
    print("<br><br><a href='Admin.html'>HOME</a>")

con.close()
