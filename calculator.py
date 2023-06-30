# create a calculator using the elif and io
print("a. addition")
print("b. subtraction")
print("c. multiplication")
print("d. division")
operation = (input("Select the operation a/b/c/d:"))
num1 = int(input("Num1:"))
num2 = int(input("Num2:"))
if operation == "a":
    print(num1, "+", num2, "=", num1 + num2)
elif operation == "b":
    print(num1, "-", num2, "=", num1 - num2)
elif operation == "c":
    print(num1, "*", num2, "=", num1 * num2)
elif operation == "d":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("invalid")
