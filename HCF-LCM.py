def hcf(x,y):
    hcf = 1
    for i in range(2,x+1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf
a = int(input('Enter num1: '))
b = int(input('Enter num2: '))
if a<b:
    print('HCF of {0} and {1} is: {2}'.format(a,b,hcf(a,b)))
    print('LCM of {0} and {1} is: {2}'.format(a,b,int(((a*b)/hcf(a,b)))))
else:
    print('HCF of {0} and {1} is: {2}'.format(a,b,hcf(b,a)))
    print('LCM of {0} and {1} is: {2}'.format(a,b,int(((a*b)/hcf(b,a)))))