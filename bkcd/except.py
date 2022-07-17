# define Python user-defined exceptions
# Create a class student with attributes roll number, name, age and course. Initialize
# the values through parameterized constructor. If the age of student is not in between
# 15 and 21 then generate user defined exception: "Age not with range exception", if
# the name contains number or a special character raise: “Name not valid exception”.
# Define the two exception classes.
import re
class agechecker(Exception):
    pass
class namechecker(Exception):
    pass
class student:
    def __init__(self,rollno,name,age,course):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.course = course
        print('age initialized to ',age)

try:
    rollno = int(input("Enter roll: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    match = re.findall("[0-9@!]",name)
    if match:
        raise namechecker
    if not 15 < age < 21:
        raise agechecker
    
    s1 = student(rollno,name,age,course)
except agechecker:
    print('age not in range bro')
except namechecker:
    print('name has number')
