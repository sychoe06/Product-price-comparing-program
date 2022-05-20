"""Get product details - First test
Used functions from 01_get_budget_v4 and 02_main_unit_v5 to help run my coding
and to check for valid numbers and words.
Uses a while loop to keep asking for product details until 'X' (which is the
exit symbol) is entered instead of a product name.
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

name = ""
print("Please enter the following details for the product\n")
while name != "X":
    # Product details
    name = input("Product name or 'X' to finish: ").title()
    if name == "X":
        break
    else:
        weight = number_checker(f"Weight of {name} (without units): ")
        unit = check_valid("The unit for weight: ", valid_units)
        price = number_checker("Price (without $ sign): ")
        print()
