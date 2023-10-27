#!C:\Users\91934\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type:text/html\n\r")
import cgi
form=cgi.FieldStorage()
n=form.getvalue('n')
em=form.getvalue('e')
ps=form.getvalue('pwd')
c=form.getvalue("p")
pe=form.getvalue("pe")
pp=form.getvalue("pp")

import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,user='root',password='admin13',database='os')
cur=db.cursor()
query="INSERT INTO stu(s_name ,email ,phone ,p_email ,p_phone ,p_word ) VALUES(%s,%s,%s,%s,%s,%s)"
val=(n,em,ps,c,pe,pp)
cur.execute(query,val)
db.commit()
db.close()

import time as t
from datetime import datetime
dt=datetime.now()
ht=dt.strftime("%H")
mt=dt.strftime("%M")
st=dt.strftime("%S")



import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,user='root',password='admin13',database='os')
cur=db.cursor()
#cur.execute ("create table time(hour varchar(20),min varchar(20),sec varchar(20))")
query="INSERT INTO time(hour,min,sec )VALUES(%s,%s,%s)"
val=(ht,mt,st)
cur.execute(query,val)
db.commit()
"""cur.execute("SELECT hour FROM time")
a=(cur.fetchone())
for x in a :
    print(x)"""




print('''
<html>
<head>
<center>
<h1>LOGIN</h2>

<body>
<form method="POST" action="tamil1.html">
<body background="l.jpg" style="background=repeat:no-repeat;background-size:100% "></body>
<body>
<table>
<tr>
<td><h2 style="color:brown">USER NAME:</h2></td>
<td><h2><input type="text align:center"; placeholder="user name"></h2></td>
</tr>
<tr>
<td><h2 style="color:brown">PASSWORD:</h2></td>
<td><h2><input type="text" placeholder="password"></h2></td>
</tr>
<tr>
<center>
<td><style="color:green"><input type="submit" value="Login"></td>
</center>
</tr>
</table>
</center>
</body>
</head>
</html>
'''
)


