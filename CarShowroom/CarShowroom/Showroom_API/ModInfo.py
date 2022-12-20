#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
import cgi
from urllib import request
import json

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
req=cgi.FieldStorage()
cartyp=req.getvalue("cartype")

print("Car Information")
response=request.urlopen("https://www.google.com/'%s'/info"%cartyp)
data=response.read()
# print(data)

info=json.loads(data)
print("Description",info)



