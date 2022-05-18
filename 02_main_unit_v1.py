"""Get main unit for products - trial 1
Asks for a main unit to use later for the weight of products and comparing
products. Keeps asking until valid unit is entered.used
"""
valid_units = ["kg", "mg", "g", "l", "kl", "ml"]
main_unit = input("Enter main unit for products: ").lower()
while main_unit not in valid_units:
    print("Please enter only 1 unit (e.g. kg, ml and etc.)\n")
    main_unit = input("Enter main unit for products: ").lower()
print("valid")  # prints "valid" for testing purposes
