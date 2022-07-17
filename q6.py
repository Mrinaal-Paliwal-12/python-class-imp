# Write a Python Program to create a list by concatenating of list.

lst = []
num = int(input('How many values in list: '))
for n in range(num):
    ch = input('Enter char: ')
    lst.append(ch)
num1 = int(input('Enter n:'))
for n in range(1,num1):
    for i in lst:
        print(i + str(n),end=" ")
