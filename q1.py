# Write a Python Program to count the number of characters (char frequency) in a string.

def continuefunc():
    ans = input("Do you want to continue? Yes/No ")
    if ans == "Yes" or ans == "yes":
        charlist()
    else:
        print("Thank you")

def charlist():
    string1 = input("Enter the string: ")
    dict = {}
    for i in string1:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
continuefunc()
