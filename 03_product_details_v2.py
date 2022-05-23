"""Based on 03_product_details_v1, (get product details)
I realised that later it will be harder to compare products if some products
have different unit measurements in its weight.
So I used For loops to check if the unit matches main unit and if it does then
convert the unit to the main unit. (line 81-115)
I also made separate lists for each of the 3 types of unit measurements.
(line 50-62)
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
# List of all valid units
valid_units = [["kg", "kilograms", "kilogram"],
               ["mg", "milligrams", "milligram"], ["g", "grams", "gram"],
               ["l", "litre", "liter", "litres", "liters"],
               ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]

# Separate list for kg and kl
kilo_units = [["kg", "kilograms", "kilogram"],
              ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"]]

# Separate list for g and L
middle_units = [["g", "grams", "gram"],
                ["l", "litre", "liter", "litres", "liters"]]


# Separate list for mg and ml
milli_units = [["mg", "milligrams", "milligram"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]

name = ""
main_unit = "kg"  # for testing purposes only
print(f"main unit: {main_unit}")
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

        # Converts units into the main unit so that the weight are all in the
        # same unit (this will help with comparing products later)

        # If unit = kg or kl
        for unit_kil in kilo_units:
            if unit in unit_kil:
                # If main unit = g or L
                for mid in middle_units:
                    if main_unit in mid:
                        new_weight = weight * 1000
                # If main unit = mg or ml
                for mil in milli_units:
                    if main_unit in mil:
                        new_weight = weight * 1000000

        # If unit = g or L
        for unit_mid in middle_units:
            if unit in unit_mid:
                # If main unit = kg or kl
                for kil in kilo_units:
                    if main_unit in kil:
                        new_weight = weight / 1000
                # If main unit = mg or ml
                for mil in milli_units:
                    if main_unit in mil:
                        new_weight = weight * 1000

        # If unit = mg or ml
        for unit_mil in milli_units:
            if unit in unit_mil:
                # If main unit = kg or kl
                for kil in kilo_units:
                    if main_unit in kil:
                        new_weight = weight / 1000000
                # If main unit = g or L
                for mid in middle_units:
                    if main_unit in mid:
                        new_weight = weight / 1000

        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: {new_weight}{main_unit}\n")

        price = number_checker("Price (without $ sign): ")
        print("-" * 40)
