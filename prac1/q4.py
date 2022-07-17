# Write a Python Program to get a string from a given string where all occurrences of its first character have been changed to ‘@’ except the first char itself.


str7=input("Enter a string ")
s1=str7[0]
str = s1 + str7[1:].replace(s1,"@")
print(str)
