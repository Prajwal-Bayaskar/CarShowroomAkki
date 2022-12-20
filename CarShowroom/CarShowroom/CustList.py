#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

print("<link rel='stylesheet'href='bootstrap.min.css'> ")
req=cgi.FieldStorage()

con=pymysql.connect(host="localhost",user="root",password="root",database="akki")
curs=con.cursor()

curs.execute("select * from Customers ")
data=curs.fetchall()


print("<div class container'>")
print("<br><br>")
print('<h2>Customer LIST</h2><hr>')
print("<a href='index.html'>Back</a><br><br>")
#print(data)

print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:azure'>")
print('<th>Customer ID')
print('<th>Customer Name')
print("<th>Car Purchased")
print("<th>Amount Paid")
print("<th>Address ")
print("<th>Mobile")

print("</tr>")

for rec in data:
    print("<tr>")
    print("<td>",rec[0])
    print("<td>",rec[1])
    print("<td>",rec[2])
    print("<td>",rec[3])
    print("<td>",rec[4])
    print("<td>",rec[5])
    print("</tr>")

print("</table")
con.close()