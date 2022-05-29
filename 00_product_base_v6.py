"""Added 05_append_details_v4 to original v5 of this base code
"""
# Import statements
import re

# Functions go here


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
                    converted_weight = weight * 1000
                    return converted_weight
            # If main unit is mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    converted_weight = weight * 1000000
                    return converted_weight

    # If unit is g or L
    for unit_mid in middle_units:
        if unit in unit_mid:
            # If main unit is kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    converted_weight = weight / 1000
                    return converted_weight
            # If main unit is mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    converted_weight = weight * 1000
                    return converted_weight

    # If unit is mg or ml
    for unit_mil in milli_units:
        if unit in unit_mil:
            # If main unit is kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    converted_weight = weight / 1000000
                    return converted_weight
            # If main unit is g or L
            for mid in middle_units:
                if main_unit in mid:
                    converted_weight = weight / 1000
                    return converted_weight
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


# ******** Main Routine ********
# Set up variables
name = ""

# Set up dictionaries / lists needed to hold data
# List for units
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

products_within_budget = []  # list for products within budget
products_above_budget = []  # list for products above budget

# Ask user if they have used the program before and
# show instructions if necessary

# Get budget
budget = number_checker("Enter budget: ")

# Get main unit for products
main_unit = check_valid("Enter main unit for products (e.g. kg, ml etc): ",
                        valid_units)

# Get product details
print("\nPlease enter the following details for the product\n")
while name != "X":
    # Product details
    name = input("Product name or 'X' to finish: ").title()
    if name == "X":
        break
    else:
        weight = number_checker(f"Weight of {name} (without units): ")
        unit = check_valid("The unit for weight: ", valid_units)

        # Unit conversion - matches main unit
        new_weight = unit_converter()
        unit = finding_l_unit(unit)  # checking if unit is "l"
        new_unit = main_unit
        new_unit = finding_l_unit(new_unit)  # checking if unit is "l"

        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: {new_weight}{new_unit}\n")
            
        price = number_checker("Price (without $ sign): ")

        # Calculate unit price - Formats to 2dp
        unit_price = "{:.2f}".format(price / new_weight)

        # Append details to list
        # Checking if product price is within or above budget
        if price <= budget:
            products_within_budget.append(
                [name, new_weight, new_unit, price, unit_price])
        else:
            products_above_budget.append(
                [name, new_weight, new_unit, price, unit_price])

        print("-" * 40)  # decoration

# Display all products details (within budget)

# Display all products outside budget

# Recommendation for "best buy"

# Save data in a file
