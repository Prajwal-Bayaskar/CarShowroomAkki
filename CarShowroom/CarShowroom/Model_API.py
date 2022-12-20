#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql


print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req = cgi.FieldStorage()
nm = req.getvalue("carmod")

con = pymysql.connect(host="localhost",user="root",password="root",database="akki")
curs = con.cursor()

curs.execute("select * from cars where modnm='%s'" % nm)
con.commit()
data = curs.fetchone()


print("<div class='container'><br>")
print("<h3>Car Information </h3>")

if data:
    print("<b>Company Name: ", data[1])
    print("<br>Model Name: ", data[2])
    print("<br>Engine power: ", data[3])
    print("<br>Fuel Type: ", data[4])
    print("<br>Car Type: ", data[5])
    print("<span style='color:green;font=weight:bold'>")
    print("<br>Price: ", data[6])
    print("</span>")
    print("<br>Color: ", data[7])
   

else:
    print("<span style='color:red;font=weight:bold'>")
    print("Car Not Found OR Out of Stock")
    print("</span>")
    print("<br><br><a href='Admin.html'>HOME</a>")

con.close()
