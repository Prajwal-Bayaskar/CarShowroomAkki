#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")

req=cgi.FieldStorage()
cnm=req.getvalue("compnm")

con=pymysql.connect(host='localhost',user='root',password='root',database='akki')
curs=con.cursor()

curs.execute("select * from Cars where compnm='%s'"%cnm)
data=curs.fetchall()

print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print("<th>Reg No.")
print("<th>Company")
print("<th>Model")
print("<th>Engine ")
print("<th>Fuel Type")
print("<th>Car Type")
print("<th>Price")
print("<th>Color")
print("</tr>")


for rec in data:
    print("<tr>")
    print("<td>",rec[0])
    print("<td>",rec[1])
    print("<td>",rec[2])
    print("<td>",rec[3])
    print("<td>",rec[4])
    print("<td>",rec[5])
    print("<td>",rec[6])
    print("<td>",rec[7])
    print("</tr>")

print("<table>")

print("<a href='AdminHome.html'>Home</a><br>")

con.close()