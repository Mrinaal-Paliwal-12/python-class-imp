# Write a Python program to create a regular expression that reads email-ids
# from a text file.
import re
f = open('final pracs/q2b.txt','r')
for i in f:
    email = re.findall(r'\S+@\S+',i)
    print(email)