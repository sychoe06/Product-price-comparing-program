"""Get budget - Second iteration of 01_get_budget_v3
Changed "ERROR" to lowercase because no capital letters are allowed in a
function. This follows the PEP8 standard.
"""


# Checks for valid positive number
def number_checker(question):
    number = -1
    error = "Please enter a positive number! No letters and can't be blank\n"
    while number < 0:
        try:
            number = float(input(question))
            if number < 0:
                print(error)
            else:
                return number
        except ValueError:
            print(error)


# Main routine
budget = number_checker("Enter budget: ")
print("valid!")  # prints "valid" for testing purposes
