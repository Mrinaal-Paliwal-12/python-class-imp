# ) Create a table EMPLOYEE with columns Id(Integer, not null, primary
# key), AdhaarNo (integer, not null), Empname (not null,varchar),Empdept
# (not null,varchar) and Empage (not null, integer) in MySQL and insert 10
# rows using parameterized query
# ii) Update the respective rows to Empdept=‟ERP‟ where Empage is >=40.
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='test')
mycur = mydb.cursor()
# mycur.execute('create table employee(id int not null primary key, adhaarno int not null,empname varchar(15) not null,empdept varchar(10) not null, empage int not null) ')
def ins():
    for i in range(2):
        eid = int(input('Enter id: '))
        adhaar = int(input('Enter adhaar: '))
        empname = input('Enter empname: ')
        empdept = input('Enter empdept: ')
        empage = int(input('Enter empage: '))
        sql = 'insert into employee(id,adhaarno,empname,empdept,empage) values(%s,%s,%s,%s,%s)'
        val = (eid,adhaar,empname,empdept,empage)
        mycur.execute(sql,val)
        mydb.commit()
# ins()
def update():
    mycur.execute('update employee set empdept=%s where id=%s',('ERZ',1))
    mydb.commit()
update()
print('done')