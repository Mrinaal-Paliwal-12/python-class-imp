# Write a method in python to display the elements of list thrice if it is a number
# and display the element terminated with '#' if it is not a number. For example,
# if the content of list is as follows: This
# List=['41','DROND','GIRIRAJ','13','ZARA']
# O/P : 414141
# DROND#
# GIRlRAJ#
# 131313
# ZARA# 

n = int(input('Enter total elements: '))
l1 = []
l2 = []
for i in range(n):
    str1 = input('Int or string?(i/o): ')
    if str1 == 'i':
        n = int(input('Enter value: '))
        l1.append(n)
        ns = str(n)
        l2.append(ns*3)
    elif str1=='o':
        s = input('enter value: ')
        l1.append(s)
        l2.append(s+'#')
print('Entered list :',l1)
print('output list :',l2)