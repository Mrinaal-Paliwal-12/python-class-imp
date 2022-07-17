import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="",database="test")
mycur = con.cursor()
# n = int(input("enter n:"))
# for i in range(1):
#     id1 = int(input("Enter id: "))
#     name = input("Enter id: ")
#     class1 =input("Enter id: ")
#     grade = input("Enter id: ")
#     sql = "insert into student (id,name,class,grade) values(%s,%s,%s,%s)"
#     val = (id1,name,class1,grade)
#     mycur.execute(sql,val)
    # con.commit()
# mycur.execute("select * from student where grade ='o'")
# row = mycur.fetchall()
# print(row)
