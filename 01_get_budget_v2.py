"""Get budget - Trial 2
Uses a number checker to make sure only numbers are entered.
And the program does not crash when strings or blanks are entered.
"""


# Checks for valid positive float (number)
def number_checker(question):
    number = -1
    while number < 0:
        try:
            number = float(input    (question))
            if number < 0:
                print("Please enter a positive integer or float!\n")
            else:
                return number
        except ValueError:
            print("Please enter a positive integer or float!\n")


budget = number_checker("Enter budget: ")
print("valid!")  # prints "valid" for testing purposes
