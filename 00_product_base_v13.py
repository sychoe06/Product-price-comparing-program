"""Added 10_instructions_v3 to v12 of this base code - post usability testing 1
This shows the post usability testing now incorporated into the assembled code
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


# Checking whether answer to question is 'Y' or 'N'
def yes_or_no(question):
    error = "Error! Please enter 'Y' or 'N' to answer this question\n"
    valid_answers = [["Y", "Yes"], ["N", "No"]]  # valid answers list
    valid = False
    while valid is False:  # assuming that answer is not valid
        answer = input(question).title()
        for answer_list in valid_answers:
            if answer in answer_list:  # if answer is in valid_answers list
                return answer_list[0]  # returns 'Y' or 'N'
        print(error)  # print error if answer is not valid


# ******** Main Routine ********
# Set up variables
name = ""

# Set up dictionaries / lists needed to hold data
total_weights_list = []  # All the weights of the products
total_prices_list = []  # All the prices of the products

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

# Ask user if they have used the program before and if not, show instructions
instructions = yes_or_no("Do you want the instructions? (Y/N): ")
if instructions == "Y":
    print("\n\t- - - - - Instructions - - - - -"
          "\nThis is a program which compares the unit prices\n"
          "of different products. It will help you be able to\n"
          "decide which product you should buy.\n\n"
          
          "Enter your budget which is the maximum limit of money\n"
          "you are willing to spend (don’t include the $ sign).\n"
          "Then enter the main unit which will convert the units\n"
          "of a product to match the main unit. This will help\n"
          "keep the units of the products all the same.\n\n"
          
          "After that enter the details of your products like...\n"
          "the name, weight, unit and price. Make sure to not\n"
          "include the $ sign for the price. And enter the\n"
          "weight and the unit of the product separately.\n\n"
          
          "Enter 'X' instead of entering the product name.\n"
          "This will display the...\n"
          "\t>> Names of each product\n"
          "\t>> Unit prices of each product\n"
          "\t>> Cheapest unit price\n"
          "\t>> Most expensive unit price\n"
          "\t>> Average unit price\n"
          "\t>> And the Best Buy\n\n"
          
          "The 'best buy' is the recommended product to buy\n"
          "because it has the cheapest unit price and is\n"
          "within your budget range.")
    print("\t", "- " * 15)

# Get budget
budget = number_checker("\nEnter budget: ")

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

        total_weights_list.append(new_weight)  # adds converted weight to list
        total_prices_list.append(price)  # adds price to list
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

# Calculate average unit price of all products
total_price = sum(total_prices_list)
total_weight = sum(total_weights_list)
average_unit_price = total_price / total_weight
print(f"\nAverage unit price of all products: {currency(average_unit_price)}")

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
save_product_details = yes_or_no("Save products details in excel files? (Y/N): ")
if save_product_details == "Y":  # If yes then save data
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
