# Self made program to check leap year
# For a leap year, it should divide by 4
# but if the year is a multiple of 100,
# It is a leap year only if it is divisible by 400
year = int(input('Enter a year:'))
if year%4==0 :
    if year%100==0:
        if year%400==0:
            print(year,'is a leap year!')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
else:
    print(year,'is not a leap year')