# 3) Write a user defined function arrangelements(X), that accepts a list X of
# integers and sets all the negative elements to the left and all positive elements
# to the right of the list. (8)
# Eg: if L =[1,-2,3,4,-5,7] , the output should be: [-2,-5,3,4,7]

def arrangel(l):
    n = len(l)
    j = 0
    for i in range(n):
        if(l[i]<0):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            j += 1
l = [1,-2,-3,4,-5,6,7,-8,9]
arrangel(l)
print(l)