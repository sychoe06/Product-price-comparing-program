"""Recommendation for "best buy" - based on 08_best_buy_v1
Placed some repeating codes into a function - this is for finding the best buy
This will help make the layout of the code look more neater and take up less
space.
"""
import pandas


# Currency formatting function for unit price only
def currency(number):
    return f"${number:,.2f} per {unit}"


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


# Finds best buy for products above or within budget
def best_buy(products_list, lowest_unit_price):
    for value in products_list:
        if value[1] == lowest_unit_price:  # finds unit price in list
            product_best_buy = value[0]  # finds name of best buy
            return product_best_buy


# Test data in lists (can change)
products_within_budget = [["Greggs", 0.04], ["Nescafe", 0.06]]
products_above_budget = [["Moccona", 0.12]]

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

unit = "g"  # unit is for testing purposes only

# Display the details of the products within the budget
display_details(products_within_budget, products_within_dict, "within")
# Display the details of the products above the budget
display_details(products_above_budget, products_above_dict, "above")

# Finding product with lowest unit price that is within the budget
lowest_unit_price_within = min(unit_price_list_within)
# Finding product with lowest unit price that is above the budget
lowest_unit_price_above = min(unit_price_list_above)

# Finding names of the products that are the best buy and not best buy
best_buy_name = best_buy(products_within_budget, lowest_unit_price_within)
not_best_buy_name = best_buy(products_above_budget, lowest_unit_price_above)
best_buy_name_one = best_buy(products_above_budget, lowest_unit_price_above)
best_buy_name_two = best_buy(products_within_budget, lowest_unit_price_within)

# Best buy and not best buy recommendation variables
best_buy_product = f"Best buy: {best_buy_name} - ${lowest_unit_price_within} "\
                   f"per {unit} and within budget"
not_best_buy = f"Cheapest unit price: {not_best_buy_name} - "\
               f"${lowest_unit_price_above} per {unit} but above budget"

# Finding the names for the products with lowest unit prices
if lowest_unit_price_above > lowest_unit_price_within:
    # Best buy is within budget with cheapest unit price
    print(best_buy_product)
elif lowest_unit_price_above < lowest_unit_price_within:
    # cheapest unit price is not best buy because it is above budget
    print(not_best_buy)
    print(best_buy_product)
else:  # If cheapest unit prices are equal, product within budget is best buy
    print(f"Cheapest unit price #1: {best_buy_name_one} - "
          f"${lowest_unit_price_above} per {unit} but above budget")
    print(f"Cheapest unit price #2: {best_buy_name_two} - "
          f"${lowest_unit_price_within} per {unit} but within budget")
    print(f"So best buy: {best_buy_name_two}\n")
