#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type: text/html")
print()

req=cgi.FieldStorage()
img=req.getvalue("file")
carno=req.getvalue("carno")
carcomp=req.getvalue("compnm")
carmod=req.getvalue("modnm")
encap=req.getvalue("encap")
ftype=req.getvalue("ftype")
cartyp=req.getvalue("cartype")
price=req.getvalue("price")
color=req.getvalue("col")
# carpic=req.getvalue("carpic")

con=pymysql.connect(host='localhost',user='root',password='root',database='akki')
curs=con.cursor()

try:
    curs.execute("insert into Cars values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(img,carno,carcomp,carmod,encap,ftype,cartyp,price,color))
    con.commit()
    print("<h3 style='color:blue'>New Car Registered successfully..!</h3>")
    
    
except Exception as e:
    print(e)
    print("<br>")
    print("<h3 style='color:red'> Registeration Failed..!</h3>")


print("<h2 style='color:green'><a href='AdminHome.html'>Home</a></h2><br>")   
con.close()