"""Based on 03_product_details_v4, (get product details) - development
I found out another small issue with my code. That is that the unit 'L' is
lowercase in my program when it should be uppercase. So I used the Regular
Expressions which is a built-in package module to check if the unit starts
with "l". And if it does start with "l" then change it to a capital "L"
"""
import re


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


# Converts product weight's unit to match main unit
def unit_converter():
    # If unit is kg or kl
    for unit_kil in kilo_units:
        if unit in unit_kil:
            # If main unit is g or L
            for mid in middle_units:
                if main_unit in mid:
                    new_weight = weight * 1000
                    return new_weight
            # If main unit is mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    new_weight = weight * 1000000
                    return new_weight

    # If unit is g or L
    for unit_mid in middle_units:
        if unit in unit_mid:
            # If main unit is kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    new_weight = weight / 1000
                    return new_weight
            # If main unit is mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    new_weight = weight * 1000
                    return new_weight

    # If unit is mg or ml
    for unit_mil in milli_units:
        if unit in unit_mil:
            # If main unit is kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    new_weight = weight / 1000000
                    return new_weight
            # If main unit is g or L
            for mid in middle_units:
                if main_unit in mid:
                    new_weight = weight / 1000
                    return new_weight
    return weight


# Checks if units are "L" or not
def finding_l_unit(check_unit):
    # Used Regular expression to test and find out if a unit starts with "l"
    finding_unit_regex = "^l"
    # Check if unit has 'l' at the start
    result = re.match(finding_unit_regex, check_unit)
    # If unit does start with "l"
    if result:
        # Then change lowercase "l" to capital letter "L"
        check_unit = "L"
        return check_unit
    # If unit does not start with "l"
    else:
        # Then return unit without changing anything
        return check_unit


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
main_unit = "kl"  # for testing purposes only
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
        converted_weight = unit_converter()
        unit = finding_l_unit(unit)
        main_unit = finding_l_unit(main_unit)

        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: "
              f"{converted_weight}{main_unit}\n")

        price = number_checker("Price (without $ sign): ")
        print("-" * 40)
