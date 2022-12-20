#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type: text/html")
print()

req=cgi.FieldStorage()
custid=req.getvalue("custid")
custnm=req.getvalue("custnm")
car=req.getvalue("car")
amt=req.getvalue("amt")
address=req.getvalue("address")
mob=req.getvalue("mob")



con=pymysql.connect(host="localhost", user="root", password="root", database="akki")
curs=con.cursor()

try:
    curs.execute("insert into Customers values('%s','%s','%s','%s','%s','%s')"%(custid,custnm,car,amt,address,mob))
    con.commit()
    print('<h3>Customer Registered Successfully...</h3>')

except Exception as e:
    print(e)
    print('<h3> Registeration Failed </h3>')
    con.close()