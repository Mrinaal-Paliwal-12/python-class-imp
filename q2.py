# Write a Python Program to get a string made of the first 2 and last 2 characters from a given string.

def continuefunc():
    ans = input("Do you want to continue? Yes/No ")
    if ans == "Yes" or ans == "yes":
        emptystring()
    else:
        print("Thank you")


def emptystring():
    str = input()
    if (len(str) < 2):
        print("String empty")
    else:
        print(str[:2] + str[-2:])

continuefunc()


