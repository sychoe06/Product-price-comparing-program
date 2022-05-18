"""Get main unit for products - trial 2
This function keeps asking for a main unit to use for the products later until
valid unit is entered.
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
