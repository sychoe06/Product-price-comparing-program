"""Get main unit for products - trial 2
This function keeps asking for a main unit to use for the products later until
valid unit is entered.
"""


# Checks for valid units
def check_units():
    valid_units = ["kg", "mg", "g", "l", "kl", "ml"]
    main_unit = input("Enter main unit for products: ").lower()
    while main_unit not in valid_units:
        print("Please enter only 1 unit (e.g. kg, ml and etc.)\n")
        main_unit = input("Enter main unit for products: ").lower()
    return main_unit


# Main routine
check_units()
print("valid")  # prints "valid" for testing purposes


