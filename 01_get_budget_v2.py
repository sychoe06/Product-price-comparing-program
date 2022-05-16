"""Get budget - Trial 2
Uses a number checker to make sure only numbers are entered.
And the program does not crash when invalid strings are entered as well.
"""


# Check for valid float (number)
def number_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("\nPlease enter a positive number! Try again")
