# Write a Python Program to Convert a list of multiple integers into a single integer.
number_list = []
n = int(input("Enter the list size "))
print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("List is ", number_list)
print("List to Single integers: ")
for i in number_list:
    print(i, end="")
