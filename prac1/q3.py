# Write a Python Program to Add suffix to the given string.

def continuefunc():
    ans = input("Do you want to continue? Yes/No ")
    if ans == "Yes" or ans == "yes":
        str_ing()
    else:
        print("Thank you")

def str_ing():
    str=input("Enter a String: ")
    if(len(str)>=3):
        if(str.endswith("ing")):
            print(str+"ly")
        else:
            print(str+"ing")
    else:
        print(str)


continuefunc()
