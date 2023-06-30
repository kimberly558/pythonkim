def Majina(fname, lname, age):
    print("My name is", fname, lname, ".", "I am ", age, "years old")


Majina("Kimberly", "Cheruto", 19)
Majina("Sasha", "Hope", 45)
Majina("Darren", "Macharia", 32)
Majina("Irene", "Asha", 10)


# create a function that calculates average of a list


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = [6, 8, 32, 78, 90, 64, 3, 34, 76]
result = calculate_average(data)
print("The average is", result)
