def add():
    x = int(input('Enter num1: '))
    y = int(input('Enter num2: '))
    print('{0} + {1} = {2}'.format(x,y,x+y))
    check()
def check():
    try:
        check = int(input('Do you want to continue?(Press 1 ,else 0) '))
        if check == 1:
            add()
        elif check==0:
            print('Thank you.')
        else:
            print('Pls enter correct values')
            rerun()
    except:
        print('Pls enter correct values')
        rerun()
def rerun():
    check()
check()