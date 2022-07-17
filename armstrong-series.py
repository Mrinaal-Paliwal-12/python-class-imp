Sterm = int(input('Enter starting index: '))
Eterm = int(input('Enter last index: '))
print('Armstrong numbers between',Sterm,'and',Eterm,'are:')
for i in range(Sterm,Eterm+1):
    num = i
    sum_num = 0
    while num!=0:
        rem = (num%10)**3
        sum_num += rem
        num //= 10
    if i==sum_num:
        print(i,end='\n')
