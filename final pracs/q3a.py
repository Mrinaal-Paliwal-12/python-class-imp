# i) Create a table Faculty with F_ID(Integer, not null, primary key), Fname
# (not null,varchar), Lname (not null,varchar), Hire_date(not null,date),
# Salary(not null,int) in SQLite3 and insert 10 rows using parameterized
# query.
# ii) To display details of those Faculties whose salary is greater than 12000?

import sqlite3
con = sqlite3.connect("teachers.db")
cur = con.cursor()
# cur.execute("""create table faculty(F_ID integer not null primary key,
#     fname text not null,lname text not null,hire_date text not null, salary integer not null
#     )""")
# for i in range(2):
#     fid = int(input("Enter id: "))
#     fname = input("Enter name: ")
#     lname = input("Enter lname: ")
#     hdate = input("Enter Hdate: ")
#     salary = int(input('enter salary:'))
#     cur.execute('insert into faculty values("'+str(fid)+'","'+fname+'","'+lname+'","'+hdate+'","'+str(salary)+'") ')
#     con.commit()
cur.execute('select * from faculty')
rows = cur.fetchall()
for i in rows:
    print(i)
print('done')
