num = int(input('Enter a number: \n'))
sum_num = 0
temp = num
while num!=0:
    rem = (num%10)**3
    sum_num += rem
    num //=10
if sum_num == temp:
    print(temp,'is armstrong number')
else:
    print(temp,'is not armstrong number')