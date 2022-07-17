Sterm = int(input('Enter starting index: '))
Eterm = int(input('Enter last index: '))
print('\nPrime numbers between ',Sterm,'and',Eterm,'are:')
if Sterm < Eterm and Sterm>=1:
    for i in range(Sterm,Eterm+1):
        flag = True
        for j in range(2,i):
            if i%j==0:
                flag = False
                break
        if flag and i!=1:
            print(i,end='\n')
else:
    print('Enter correct index values')