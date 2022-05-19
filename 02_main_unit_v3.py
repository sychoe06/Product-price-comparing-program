"""Get main unit for products - Trial 3
Uses a parameter "question" so that the question for entering the main unit
is only written in the full sentence once in the code instead of twice.
"""


# Checks for valid units
def check_units(question):
    valid_units = ["kg", "mg", "g", "l", "kl", "ml"]
    response = input(question).lower()
    while response not in valid_units:
        print("Please enter only 1 unit (e.g. kg, ml and etc.)\n")
        response = input(question).lower()
    return response


# Main routine
main_unit = check_units("Enter main unit for products: ")
print("valid")  # prints "valid" for testing purposes
