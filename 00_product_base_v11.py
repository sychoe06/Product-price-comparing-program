"""Added 09_save_data_in_file_v4 to original v10 of this base code
This code is the Assembled outcome program before the usability testing!

Edited the recommendation for best buy coding to make sure that the program
does not crash when there are no products entered, no products above the budget
or no products within the budget. Also made the display details function to
return the product_frame.
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
    error = "Sorry that is not a valid answer\n"
    getting_option = "yes"
    while getting_option == "yes":
        response = input(question).lower()
        for option in valid_options:
            if response in option:  # if answer is in valid_answers list
                return option[0]
        print(error)


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
    return f"${number:,.2f} per {main_unit}"


# Display product details function (for products within or above budget)
def display_details(products_list, products_dict, within_or_above):
    # If there are no products that are above or within budget...
    if len(products_list) == 0:  # Then tell the user this.
        print(f"\nNo products were {within_or_above} the budget")
    else:
        # Display all products details
        # Adds product details from list into the lists inside the dictionary
        for details in products_list:
            products_dict["Name"] += [details[0]]  # Adds name
            products_dict["Unit Price"] += [details[1]]  # Adds unit price

        # Prints Product details in a well formatted way
        print(f"\n*** Products {within_or_above} the budget ***\n")
        product_frame = pandas.DataFrame(products_dict)  # create data frame

        # Changes index to reference names rather than an actual index number
        product_frame = product_frame.set_index("Name")

        # Sorts the data frame in ascending order of the unit prices
        product_frame = product_frame.sort_values("Unit Price")

        # Formats the unit prices in currency and unit price format
        # so that they have $'s and the per unit (e.g. $0.25 per g)
        # "currency" is the call to the currency() function above
        product_frame["Unit Price"] = \
            product_frame["Unit Price"].apply(currency)

        print(product_frame)  # Prints data frame
        print()
        return product_frame


# Finds best buy for products above or within budget
def best_buy(products_list, lowest_unit_price):
    for value in products_list:
        if value[1] == lowest_unit_price:  # finds unit price in list
            product_best_buy = value[0]  # finds name of best buy
            return product_best_buy


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

yes_no = [["y", "yes"], ["n", "no"]]  # valid yes and no list

products_within_budget = []  # list for products within budget
products_above_budget = []  # list for products above budget

# Creates separate list for name and unit price for the products within budget
name_list_within = []
unit_price_list_within = []

# Creates separate list for name and unit price for the products above budget
name_list_above = []
unit_price_list_above = []

# Creates the products within budget dictionary with a label and then
# a list for the product details like name and unit price
products_within_dict = {
    "Name": name_list_within,
    "Unit Price": unit_price_list_within
}

# Creates the products above budget dictionary with a label and then
# a list for the product details like name and unit price
products_above_dict = {
    "Name": name_list_above,
    "Unit Price": unit_price_list_above
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

print()
print("-" * 50)

main_unit = finding_l_unit(main_unit)  # checks if main_unit is 'l' or not

# Display the details of the products within the budget
product_frame_within = display_details(products_within_budget,
                                       products_within_dict, "within")
# Display the details of the products above the budget
product_frame_above = display_details(products_above_budget,
                                      products_above_dict, "above")

# Recommendation for "best buy"
print("\n---- BEST BUY RECOMMENDATION ----")
# If there have been no product details entered means no unit prices
if len(unit_price_list_above) == 0 and len(unit_price_list_within) == 0:
    print("There is no best buy because\nno products have been entered!\n")
    print("-" * 50)
    quit()  # this is a built in function - makes program end
else:
    # No products within budget means there are no unit prices within budget
    if len(unit_price_list_within) == 0:
        # Finding lowest unit price
        lowest_unit_price_above = min(unit_price_list_above)
        # Finding name for product with lowest unit price
        not_best = best_buy(products_above_budget, lowest_unit_price_above)

        print(f"{not_best} has cheapest unit price "
              f"({currency(lowest_unit_price_above)})\nBut is not best buy "
              f"because it is above your budget.\nSo there is no best buy!")
    # No products above budget means there are no unit prices above budget
    elif len(unit_price_list_above) == 0:
        # Finding lowest unit price
        lowest_unit_price_within = min(unit_price_list_within)
        # Finding name for product with lowest unit price
        best = best_buy(products_within_budget, lowest_unit_price_within)

        print(f"Best buy is {best} ({currency(lowest_unit_price_within)})")
    else:
        # Finding lowest unit prices
        lowest_unit_price_above = min(unit_price_list_above)
        lowest_unit_price_within = min(unit_price_list_within)
        # Finding name for product with lowest unit prices
        best = best_buy(products_within_budget, lowest_unit_price_within)
        best_one = best_buy(products_above_budget, lowest_unit_price_above)
        best_two = best_buy(products_within_budget, lowest_unit_price_within)
        not_best = best_buy(products_above_budget, lowest_unit_price_above)

        recommend_best_buy = f"Best buy is {best} " \
                             f"({currency(lowest_unit_price_within)})"

        # Best buy is within budget with cheapest unit price
        if lowest_unit_price_above > lowest_unit_price_within:
            print(recommend_best_buy)
        # cheapest unit price is not best buy because it is above budget
        elif lowest_unit_price_above < lowest_unit_price_within:
            print(f"{not_best} has cheapest unit price "
                  f"({currency(lowest_unit_price_above)})\nBut is not "
                  f"best buy because it is above your budget.\n")
            print(recommend_best_buy)
        # If cheapest unit prices are equal, product within budget is best buy
        else:
            print(f"Both {best_one} and {best_two} have same\n cheapest unit "
                  f"price {currency(lowest_unit_price_within)}\n\nBut "
                  f"{best_one} is above the budget\nSo best buy is {best_two}")
print("-" * 35, "\n")

# Save data in a file
save = check_valid("Save products details in excel files? (Y/N): ", yes_no)
if save == "y":  # If yes then save data
    # If there are no products within budget...
    if len(products_within_budget) == 0:
        # Write frame to csv file for products above budget
        product_frame_above.to_csv("products_above_budget.csv")
        print("\nProducts details have been saved to an excel file!\n")
        print("Note: To see saved details of products find an\nexcel file "
              "called products_above_budget.csv\n")
    # If there are no products above budget...
    elif len(products_above_budget) == 0:
        # Write frame to csv file for products within budget
        product_frame_within.to_csv("products_within_budget.csv")
        print("\nProducts details have been saved to an excel file!\n")
        print("Note: To see saved details of products find an\nexcel file "
              "called products_within_budget.csv\n")
    else:
        # Write each frame to separate csv files for within and above
        product_frame_within.to_csv("products_within_budget.csv")
        product_frame_above.to_csv("products_above_budget.csv")
        print("\nProducts details have been saved to excel files!\n")
        print("Note: To see saved details of products find excel files called "
              "\nproducts_within_budget.csv and products_above_budget.csv\n")
else:  # If no then don't save data
    print("\nProducts details have NOT been saved to excel files!\n")
print("-" * 50)
