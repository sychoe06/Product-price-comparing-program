"""Based on 01_get_budget_v2, (get budget)
I developed trial 2 further by using a constant "ERROR" for the error message
so that it can be more helpful for future proofing/editing.
I also changed the error message so that normal users can understand what the
error means.
"""


# Checks for valid positive number
def number_checker(question):
    number = -1
    ERROR = "Please enter a positive number! No letters and can't be blank\n"
    while number < 0:
        try:
            number = float(input(question))
            if number < 0:
                print(ERROR)
            else:
                return number
        except ValueError:
            print(ERROR)


# Main routine
budget = number_checker("Enter budget: ")
print("valid!")  # prints "valid" for testing purposes
