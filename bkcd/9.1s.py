# Create a table STUDENT with columns id (integer, not null, primary key),
# Rollno (integer, not null), Name (not null, varchar), class (not null, varchar)
# and Grade (not null, varchar) in MySQL and insert 10 rows of data using
# parameterized query.
import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='',database='test')
print('connected')
mycur = conn.cursor()
# mycur.execute('create table student(id integer not null primary key,name varchar(20) not null ,class varchar(20) not null, grade varchar(25) not null)')
# print('table created successfully!')
sql ="insert into student (id,name,class,grade) values(%s,%s,%s,%s)"
id = 2
name = "sayali"
myclass = "mca"
grade = "O"
val = (id, name,myclass,grade)
mycur.execute(sql, val)
conn.commit()