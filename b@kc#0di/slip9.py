import threading
n = int(input('enter n:\n'))

def factorial(num):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print('Factorial is ',fact,end='\n')
def fibo(num):
    a = 0
    b = 1
    print('\n',a,'\n',b,'\n',sep='')
    for i in range(num-2):
        c = a+b
        print(c,'\n')
        a = b
        b = c

t1 = threading.Thread(target=factorial, args=(n,))
t1.start()
t2 = threading.Thread(target=fibo, args=(n,))
t2.start()

print("Done!")

