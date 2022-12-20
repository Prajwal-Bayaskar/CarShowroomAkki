#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
id=req.getvalue("uid")
ps=req.getvalue("psw")

con=pymysql.connect(host='localhost',user='root',password='root',database='akki')
curs=con.cursor()

curs.execute("select * from Users where userid='%s' and pswd='%s'"%(id,ps))
data=curs.fetchone()

if data:
    #print('<h3>Welcome to  Python web development</h3>')
    
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=AdminHome.html'/>")
    print("</head>")
    print("</html>")
    
else:
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=Failure.html'/>")
    print("</head>")
    print("</html>")

    #print('<h3>Sorry Authentication Failed</h3>')

con.close()