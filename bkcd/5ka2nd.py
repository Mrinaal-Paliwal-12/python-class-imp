# Write a Python program to list all the factorial numbers less than or equal to an
# input number n. Use recursive function to calculate factorial. (10)
# A number N is called a factorial number if it is the factorial of a positive integer.
# For example, the first few factorial numbers are
# 1,2,6,24,120 ….
# Note : We do not list the factorial of 0.
# Input : A positive integer, say n.
# Output: All factorial numbers less than or equal to n.
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n1 = int(input("enter num1 "))
n2 = int(input("enter num2 "))
if n2>n1:
    print("factorials between",n1,"and",n2,"are:\n")
    for i in range(1,n2):
        if n2>fact(i)>n1:
            print(fact(i))
