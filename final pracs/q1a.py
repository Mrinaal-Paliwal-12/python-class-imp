# 1. Write a Python program to do the following: (12)
# i) Create a table STUDENT with columns id (integer, not null, primary key),
# Rollno (integer, not null), Name (not null, varchar), class (not null, varchar)
# and Grade (not null, varchar) in MySQL and insert 10 rows of data using
# parameterized query.
# ii) Retrieve the rows where Grade=‟O‟
import mysql.connector
con = mysql.connector.connect(host='localhost',user="root",password="",database='test')
mycur = con.cursor()
def ins():
    n = int(input('enter num of records:'))
    for i in range(n):
        sid = int(input('enter id: '))
        name = input('enter name: ')
        sclass = input('enter sclass: ')
        grade = input('enter grade: ')
        sql = 'insert into student(id,name,class,grade) values(%s,%s,%s,%s)'
        val = (sid,name,sclass,grade)
        mycur.execute(sql,val)
        con.commit()
# ins()
def retrieve():
    mycur.execute('select * from student where grade="o"')
    rows = mycur.fetchall()
    for i in rows:
        print(i)
retrieve()
print('done')