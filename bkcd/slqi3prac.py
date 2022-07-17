import sqlite3


import sqlite3
conn = sqlite3.connect('employee.db')

mycur = conn.cursor()

# mycur.execute("""create table employees(
#     first text,
#     last text,
#     pay integer
#     )""")
mycur.execute("insert into employees values('kunal','paliwal','12000')")
conn.commit()
mycur.execute("select * from employees where last='paliwal'")
print(mycur.fetchall())

conn.commit()
conn.close()