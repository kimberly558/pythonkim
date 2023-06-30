# create  a python project to check if a given year is a leap year
# yr is divisible by 4 but not divisible by100
# except if its also divisible by 400

year = int(input("Enter the year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Year is leap year")
else:
    print("Year is not a leap year")