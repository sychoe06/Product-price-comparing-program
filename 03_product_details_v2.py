"""Get product details - iteration of the first test
I use Python's RE tool to help analyse the given string, work out whether or
not it contains number, and then separate the string into number (weight)
and item (unit).
If no specific unit is provided then assumes that unit is the main unit
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
kilo_units = [["kg", "kilograms", "kilogram"],
              ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"]]
milli_units = [["mg", "milligrams", "milligram"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]
middle_units = [["g", "grams", "gram"],
                ["l", "litre", "liter", "litres", "liters"]]

name = ""
main_unit = "kg"  # for testing purposes only
print("Please enter the following details for the product\n")
while name != "X":
    # Product details
    name = input("Product name or 'X' to finish: ").title()
    if name == "X":
        break
    else:
        weight = number_checker(f"Weight of {name} (without units): ")
        unit = check_valid("The unit for weight: ", valid_units)
        new_weight = weight
        for unit_kil in kilo_units:
            if unit in unit_kil:
                for mid in middle_units:
                    if main_unit in mid:
                        new_weight = weight * 1000
                for mil in milli_units:
                    if main_unit in mil:
                        new_weight = weight * 1000000
        for unit_mid in middle_units:
            if unit in unit_mid:
                for kil in kilo_units:
                    if main_unit in kil:
                        new_weight = weight / 1000
                for mil in milli_units:
                    if main_unit in mil:
                        new_weight = weight * 1000
        for unit_mil in milli_units:
            if unit in unit_mil:
                for kil in kilo_units:
                    if main_unit in kil:
                        new_weight = weight / 1000000
                for mid in middle_units:
                    if main_unit in mid:
                        new_weight = weight / 1000

        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: {new_weight}{main_unit}\n")

        price = number_checker("Price (without $ sign): ")
        print("-" * 40)
