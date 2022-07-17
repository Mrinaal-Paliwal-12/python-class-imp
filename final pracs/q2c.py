# Write a Python program to read a line of text from the console. Print only the
# vowels and the position of the vowel.
import json
from textwrap import indent
str = input('Enter a string:')
dict={
    'a':['total occurences: ',0,'indexes: '],
    'e':['total occurences: ',0,'indexes: '],
    'i':['total occurences: ',0,'indexes: '],
    'o':['total occurences: ',0,'indexes: '],
    'u':['total occurences: ',0,'indexes: ']
}
index = 0
for i in str:
    if i == 'a' or i == 'A':
        dict['a'][1] += 1
        dict['a'].append(index)
    if i == 'e' or i == 'E':
        dict['e'][1] += 1
        dict['e'].append(index)
    if i == 'i' or i == 'I':
        dict['i'][1] += 1
        dict['i'].append(index)
    if i == 'o' or i == 'O':
        dict['o'][1] += 1
        dict['o'].append(index)
    if i == 'u' or i == 'U':
        dict['u'][1] += 1
        dict['u'].append(index)
    index+=1

print(json.dumps(dict,indent=4))