word = input("enter a word and i will count the letters you specify!\n: ")
letter = input("Enter the letter you want to count in the above string: ")
count = 0
if len(letter) ==1:
    for i in word:
        if i == letter:
            count +=1

print(count)            