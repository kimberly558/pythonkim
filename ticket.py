#write a python program to calculate the ticket price for a movie theatre based on age
#0-5 free 6-12 500 13-17 1000 18+ 1500

age=int(input("Enter your age:"))
if age<=5:
    print("Ticket is free")
elif age>5 and age<=12:
    print("Ticket is 500")
elif age>12 and age<=17:
    print("Ticket is 1000")
elif age>=18:
    print("Ticket price is 1500")

