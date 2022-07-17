# Write a user defined function in Python that displays the number of lines starting
# with “H” in the file Para.txt
import re

f = open('final pracs/q2b.txt','r')
def checkH(f):
    count = 0
    for line in f:
        if str(line).startswith('h'):
            count+=1
    return count
print('Total lines starting with H: ',checkH(f))