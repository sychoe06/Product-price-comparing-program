"""Get main unit for products - First iteration of trial 4
Made the list for "valid_units" more flexible by adding different variations
of the units that way there is more than one way to enter a unit.
Also made an "error" constant (in lowercase) for the error message.
"""


# Checks for valid units
def check_units(question, valid_choices):
    error = "Sorry that is not a valid choice\n"
    response = input(question).lower()
    for unit in valid_choices:
        if response in unit:
            response = unit[0].lower()
            return response

    print(error)
    return check_units(question, valid_choices)


# Main routine
valid_units = [["kg", "kilograms", "kilogram"],
               ["mg", "milligrams", "milligram"], ["g", "grams", "gram"],
               ["l", "litre", "liter", "litres", "liters"],
               ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]
getting_unit = True
while getting_unit is True:
    main_unit = check_units("Enter main unit for products (e.g. kg, ml etc): ",
                            valid_units)
    getting_unit = False
print("valid")  # prints "valid" for testing purposes
