# capitalize() Converts the first character to upper-case
# casefold() Converts string into lower case
# count() Returns the number of times a specified value occurs in a string
# endswith() Returns true if the string ends with the specified value
# find() Searches the string for a specified value and returns
#           the position of where it was found.
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# split()	Splits the string at the specified separator, and returns a list
# startswith()	Returns true if the string starts with the specified value
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
mystr = "mrinaal paliwal"
print("mystr: {0} ||=||   capitalize(): {1}".format(mystr,mystr.capitalize()))
mystr = "MRINAAL PALIWAL"
print("mystr: {0} ||=||   casefold(): {1}".format(mystr,mystr.casefold()))
mystr = "Mrinaal Paliwal Kunal Paliwal Seema Paliwal Pankaj Paliwal"
print("mystr: {0} ||=||   count('Paliwal'): {1}".format(mystr,mystr.count('Paliwal')))
mystr = "Hello world!"
print("mystr: {0} ||=||   endswith('!'): {1}".format(mystr,mystr.endswith('!')))
mytuple = ("Mrinaal","Paliwal")
mystr = "-".join(mytuple)
print("mytuple: {0} ||=||   '-'.join(mytuple): {1}".format(mytuple,mystr))
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print("txt: {0} , x = txt.partition('bananas'): {1}".format(txt,x))
print("mystr: {0} ||=||   replace('Mrinaal,'Kunal'): {1}".format(mystr,mystr.replace('Mrinaal','Kunal')))
txt = "welcome to the jungle"
x = txt.split()
print("txt: {0} , x = txt.split(''): {1}".format(txt,x))
print("mystr: {0} ||=||   startswith('M'): {1}".format(mystr,mystr.startswith('M')))
print("mystr: {0} ||=||   swapcase(): {1}".format(mystr,mystr.swapcase()))
mystr = "mrinaal paliwal"
print("mystr: {0} ||=||   title(): {1}".format(mystr,mystr.title()))
