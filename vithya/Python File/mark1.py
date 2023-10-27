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

if a=="chest":
    m+=1
else:
    pass
 
if b=="Ya":
    m+=1
else:
    pass

if c=="8":
    m+=1
else:
   pass

if d=="Five":
    m+=1
else:
   pass

if e=="Maam pinju-Mavadu":
    m+=1
else:
   pass
if f=="received":
    m+=1
else:
   pass
if g=="love":
    m+=1
else:
   pass

print("<center><h1 style='color:green;'>Result<br><br>mark obtained",m,"</h1>")
print('''
<head>
    <style>
       body{
background-image: url('mark.jpg');
backgorund-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}
</style>
<body>
<form method="POST" action="home.html">
<br><h1 style="color:purple" >To goto Next language Click</h1>
<input type="submit" value="Next" style="font-size:30px;font-family:calibiri;background-color:Salmon;color:white">
<br><br>
<a href="tamil1.html"style="color:Turquoise;font-size:18">Back to home</a>
</center>
</form>
</body>
''')




mark=m
import smtplib
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='learn')
cur=db.cursor()
cur.execute("SELECT p_email FROM students")
a=(cur.fetchall())
#for x in a:
#parent=x



db=mysql.connector.connect(host='localhost',user='root',password="admin13",database='learn')
std=db.cursor()
std.execute("SELECT s_name FROM students")
b=(std.fetchall())
#for y in b:
 # s_n=y



sender="vithyaksraj1311@gmail.com"
password="jqspbvczthikaflo"
receiver="vithyaq1311@gmail.com"

connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(sender,password)
msg="login and completed chapter 1 /n scored mark in the assesment"+str(mark)

connection.sendmail(sender,receiver,msg)
