import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,user='root',password='admin13',database='os')
cur=db.cursor()
query="INSERT INTO s(s_name ,email ,phone ,p_email ,p_phone ,p_word ) VALUES(%s,%s,%s,%s,%s,%s)"
val=(n,em,ps,c,pe,pp)
cur.execute(query,val)
db.commit()
db.close()
