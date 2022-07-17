x = int(input('Enter a number: '))
val = x
sTrev_x = ''
while x!=0:
    temp = x%10
    sTrev_x += str(temp)
    x = x // 10
inTsTrev_x = int(sTrev_x)
print("Reverse of {0} is {1}".format(val,inTsTrev_x))
print(type(inTsTrev_x))