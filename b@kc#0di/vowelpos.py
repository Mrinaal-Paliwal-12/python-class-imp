# Write a Python program to read a line of text from the console. Print only the
# vowels and the position of the vowel.
str = input('Enter string: ')
lstr = str.lower()
lst = '1'+lstr
na = 0
ne = 0
ni = 0
no = 0
nu = 0
index = 0
mydict = {
    'a':[0],
    'e':[0],
    'i':[0],
    'o':[0],
    'u':[0],
}
for i in lstr:
    if i=='a':
        na+=1
        mydict['a'][0]=na
        mydict['a'].append(index)
    if i=='e':
        ne+=1
        mydict['e'][0]=ne
        mydict['e'].append(index)
    if i=='i':
        ni+=1
        mydict['i'][0]=ni
        mydict['i'].append(index)
    if i=='o':
        no+=1
        mydict['o'][0]=no
        mydict['o'].append(index)
    if i=='u':
        nu+=1
        mydict['u'][0]=nu
        mydict['u'].append(index)
    index+=1

print(mydict)