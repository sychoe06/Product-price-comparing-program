"""Based on 02_main_unit_v4, (Get main unit for products)
Made the list for "valid_units" more flexible by adding different variations
of the units that way there is more than one way to enter a unit.
Also made an "error" constant (in lowercase) for the error message.
In order to prevent any errors I also put in examples of units to enter in the
input statement and changed the error message to being more generic
"""


# Checks for valid options
def check_valid(question, valid_options):
    error = "Sorry that is not a valid choice\n"
    getting_option = "yes"
    while getting_option == "yes":
        response = input(question).lower()
        for option in valid_options:
            if response in option:
                response = option[0].lower()
                return response

        print(error)
        return check_valid(question, valid_options)


# Main routine
valid_units = [["kg", "kilograms", "kilogram"],
               ["mg", "milligrams", "milligram"], ["g", "grams", "gram"],
               ["l", "litre", "liter", "litres", "liters"],
               ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]
main_unit = check_valid("Enter main unit for products (e.g. kg, ml etc): ",
                        valid_units)
print("valid")  # prints "valid" for testing purposes
