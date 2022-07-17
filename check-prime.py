num = int(input('Enter a number: '))
if num == 1 :
    print('1 is composite number')
elif num == 2 :
    print('2 is the only even prime number!')
elif num>2 :
    flag = True
    for i in range(2,num):
        if num%i==0:
            flag = False
            break
    if flag:
        print(num,'is Prime')
    else:
        print(num,'is Non prime')
else:
    print('Enter +ve values please')
