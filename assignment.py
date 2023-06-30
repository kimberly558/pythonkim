# create a function to display the palindrome
# create a function that gives the longest string in a list of items
string = input("Enter a word:")
if string == string[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
