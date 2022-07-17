import re
f1 = open('salaries.txt','r')
f2 = open('newfile.txt','w')

for line in f1:
    res1=re.search(r'\d{4}',line)   #extract id from f1
    res2=re.search(r'\d{4,}.\d{2}',line)   #extract salary from f1
    print(res1.group(),res2.group())        #display items
    f2.write(res1.group()+"\t")          #write id no into f2
    f2.write(res2.group()+"\n")          #write salary into f2

f1.close()
f2.close()