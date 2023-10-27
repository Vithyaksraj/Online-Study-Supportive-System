#!C:\Users\91934\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\python.exe
print("Content-type:text/html\n\r")
import cgi
form=cgi.FieldStorage()
n=form.getvalue('n')
em=form.getvalue('e')
ps=form.getvalue('pwd')
c=form.getvalue("p")
pe=form.getvalue("pe")
pp=form.getvalue("pp")
print('dD')

print('''
<html>
<head>
<title>
sign in page
</title>
<center>
<h1 style="color:maroon">SIGN UP</h1>
</center>
</head>
<form action="login.html">
<body background="4.jpg" style="background=repeat:no-repeat;background-size:100% 110%"></body>
<body>
<div align = "center">
<table>
<tr>
<td><h2 style="color:violet">NAME:</h2></td>
<td><h2><input type="text" name="n" placeholder="enter name"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">D.O.B:</h2></td>
<td><h2><input type="date" name="d"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">CONTACT:</h2></td>
<td><h2><input type="phone" name="p" placeholder="phone number"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">EMAI ID:</h2></td>
<td><h2><input type="text" name="e" placeholder="enter email id"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">GENDER:</h2></td>
<td><h2><input type="radio" name="Gender" value="male">Male</h2></td>
<td><h2><input type="radio" name="Gender" value="female">Female</h2></td>
</tr>
<tr>
<td><h2 style="color:violet">PARENT EMAI ID:</h2></td>
<td><h2><input type="text" name="pe" placeholder="enter Pemail id"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">PARENT PHONE NUM:</h2></td>
<td><h2><input type="phone" name="pp" placeholder="phone number"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">PASSWORD:</h2></td>
<td><h2><input type="password" name="pwd"></h2></td>
</tr>
<tr>
<td><h2 style="color:violet">CONFORM PASSWORD:</h2></td>
<td><h2><input type="password" name="cp"></h2></td>
</tr>
<td style="color:Orchid"><input type="submit" value="Submit"></td>
<td style="color:red" >Already a user ?<a href="login.html">Login</a>
</td>

</table>
</form>
</body>
</html>
'''
)
import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,user='root',password='admin13',database='os')
cur=db.cursor()
query="INSERT INTO stu(s_name ,email ,phone ,p_email ,p_phone ,p_word ) VALUES(%s,%s,%s,%s,%s,%s)"
val=(n,em,ps,c,pe,pp)
cur.execute(query,val)
db.commit()
db.close()

#print("inserted")
