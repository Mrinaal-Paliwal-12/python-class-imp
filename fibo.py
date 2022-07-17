a = 0
b = 1
n = int(input('Enter number of terms:\n'))
if n>=2:
    print('Term 1 is :',a,'\nTerm 2 is :',b,end='\n')
    for i in range(n-2):
        c = a + b
        print('Term ',i+3,' is : ',c,end='\n',sep='')
        a = b
        b = c
elif n<2:
    print('Number of Terms less then 2!')
