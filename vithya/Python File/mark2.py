#!C:\Users\91934\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\n\r")

import cgi
form= cgi.FieldStorage()
m=0
a=form.getvalue('one')
b=form.getvalue('two')
c=form.getvalue('three')
d=form.getvalue("four")
e=form.getvalue('five')
f=form.getvalue('six')
g=form.getvalue('seven')

if a=="simple present":
    m+=1
else:
    pass
 
if b=="simple past":
    m+=1
else:
    pass

if c=="simple present":
    m+=1
else:
   pass

if d=="present":
    m+=1
else:
   pass

if e=="will-future":
    m+=1
else:
   pass
if f=="past perfect":
    m+=1
else:
   pass
if g=="if i am":
    m+=1
else:
   pass

print("<center><h1 style='color:green;'>Result<br><br>mark obtained",m,"</h1>")
print('''
<head>
    <style>
       body{
background-image: url('mark2.jpg');
backgorund-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}
</style>
<body>
<form method="POST" action="tamil1.html">
    <br><h1 style="color:maroon" >To goto Next language Click</h1>
<input type="submit" value="Next" style="font-size:30px;font-family:calibiri;background-color:Orchid;color:Cyan">
<br><br>
<a href="home.html"style="color:blue;font-size:18">Back to home</a>
</center>
</form>
</body>
''')



import time as t
from datetime import datetime
dt=datetime.now()
ht=dt.strftime("%H")
mt=dt.strftime("%M")
st=dt.strftime("%S")
h1=int(ht)
m1=int(mt)
s1=int(st)

mark=m
import smtplib
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='os')
cur=db.cursor()
cur.execute("SELECT hour FROM time")
a=cur.fetchone()
for x in a:
 pa=x

x1=int(pa)
print(type(x1))
one=x1-h1


db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='os')
cur=db.cursor()
cur.execute("SELECT min FROM time")
b=cur.fetchone()
for x in b:
 ma=x

x2=int(ma)
print(type(x2))
two=x2-m1

db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='os')
cur=db.cursor()
cur.execute("SELECT sec FROM time")
c=cur.fetchone()
for x in c:
 na=x

x3=int(na)
print(type(x3))
three=x3-s1



sender="vithyaksraj1311@gmail.com"
password="jqspbvczthikaflo"
receiver="vithyaksraj1311@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(sender,password)
msg= str(one)+ str(two)+ str(three)+"login and completed english video and scored mark is"+str(mark)

connection.sendmail(sender,receiver,msg)
