"""Added 06_products_within_budget_v3 to original v6 of this base code
I also made sure that the unit price is a float on line 189 or else the
currency formatting for the unit prices in the data frame does not work.
"""
# Import statements
import re
import pandas

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


# Currency formatting function for unit price only
def currency(number):
    return f"${number:,.2f} per {unit}"


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

# Creates separate list for name and unit price for the products
name_list = []
unit_price_list = []

# Put the separate lists above into a master list
product_list = [name_list, unit_price_list]

# Creates the products within budget dictionary with a label and then
# a list for the product details like name and unit price
products_within_dict = {
    "Name": name_list,
    "Unit Price": unit_price_list
}


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
        unit_price = float(unit_price)  # makes sure that unit price is float

        # Append details to list
        # Checking if product price is within or above budget
        if price <= budget:
            products_within_budget.append([name, unit_price])
        else:
            products_above_budget.append([name, unit_price])

        print("-" * 40)  # decoration

# Display all products details (within budget)
print("-" * 60)
# Adds the product details from list into the lists inside the dictionary
for details in products_within_budget:
    products_within_dict["Name"] += [details[0]]  # Adds name
    products_within_dict["Unit Price"] += [details[1]]  # Adds unit price

# Prints Product details in a well formatted way
print("\n*** Products within the budget ***\n")
product_frame = pandas.DataFrame(products_within_dict)  # creates data frame

# Changes the index to reference the names rather than an actual index number
product_frame = product_frame.set_index("Name")

# Sorts the data frame in ascending order of the unit prices
product_frame = product_frame.sort_values("Unit Price")

# Formats the unit prices in currency and unit price format
# so that they have $'s and the per unit (e.g. $0.25 per g)
# "currency" is the call to the currency() function above
product_frame["Unit Price"] = product_frame["Unit Price"].apply(currency)

print(product_frame)  # Prints data frame
print("-" * 60)

# Display all products outside budget

# Recommendation for "best buy"

# Save data in a file
