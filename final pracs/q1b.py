# Create a class student with attributes roll number, name, age and course. Initialize
# the values through parameterized constructor. If the age of student is not in between
# 15 and 21 then generate user defined exception: "Age not with range exception", if
# the name contains number or a special character raise: “Name not valid exception”.
# Define the two exception classes.
import re
class student:
    def __init__(self,roll,name,age,course):
        self.roll = roll
        self.name = name
        self.age = age
        self.course =course
        print('Entered values are -\nRoll-no: {0}\nName: {1}\nAge: {2}\nCourse: {3}'.format(roll,name,age,course))
class ageException(Exception):
    pass
class nameException(Exception):
    pass
try:
    roll = int(input('enter roll: '))
    name = input('enter name: ')
    age = int(input('enter age: '))
    course = input('enter course: ')
    if not 15<age<21:
        raise ageException
    match = re.findall('[0-9@!#$%^&*]',name)
    if match:
        raise nameException
    s1 = student(roll,name,age,course)
except ageException:
    print('Age not valid!')
except nameException:
    print('name not valid!')