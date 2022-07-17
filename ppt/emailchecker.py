import re
f = open('mails.txt','r')

for line in f:
    res = re.findall(r'\S+@\S+',line)
    if len(res)>0:
        print(res)

f.close()