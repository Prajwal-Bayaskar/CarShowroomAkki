#!C:\Users\aksha\AppData\Local\Programs\Python\Python39\python
from urllib import request
import json

print("Content-type:text/html")
print()

print("<link rel='stylesheet' href='bootstrip.min.css'>'")
print("<div class='container'><bR><br>")
print("<h3>Players in IPL</h3><hr>")
response=request.urlopen("http://sohamspring.azurewebsites.net/api/players")
data=response.read()
info=json.loads(data)

#print(info)

print("<ul>")
for pl in info:
    print("<li>%s(%s) plays for %s as %s" %(pl['playernm'],pl['country'],pl['club'],pl['position']))

    print("</ul>")