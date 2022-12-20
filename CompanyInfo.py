#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi

print("Content-type:text/html")
print()

req=cgi.FieldStorage()
nm=req.getvalue("comp")

print('Company Name: %s' %nm)