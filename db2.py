import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='',database='test')
print("connected to db ")
mycursor=conn.cursor()

n=int(input("how many ?"))
for i in range(n):
    name=input("name:")
    sql="insert into lavda(name) values(%s)"
    val=(name)
    mycursor.execute(sql,val)
print("inserted")
conn.commit()