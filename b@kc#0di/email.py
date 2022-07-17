import re
f = open('bkcd/mail.txt','r')

for line in f:
    res = re.findall(r'\S+@\S+',line)
    if len(res)>0:
        print(res)

f.close()
# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))