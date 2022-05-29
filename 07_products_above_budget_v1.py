"""Display products above budget - based on 06_products_within_budget_v3
Basically does the same things as component 6 but instead this is for the
products where its price's are over the budget.
"""
import pandas


# Currency formatting function for unit price only
def currency(number):
    return f"${number:,.2f} per {unit}"


# Creates separate list for name and unit price for the products
name_list = []
unit_price_list = []

# Put the separate lists above into a master list
product_list = [name_list, unit_price_list]

# Test data list
products_within_budget = [["Greggs", 0.04],
                          ["Moccona", 0.12],
                          ["Nescafe", 0.04]]

unit = "g"  # unit is for testing purposes only

# Creates the products within budget dictionary with a label and then
# a list for the product details like name and unit price
products_above_dict = {
    "Name": name_list,
    "Unit Price": unit_price_list
}

# Adds the product details from list into the lists inside the dictionary
for details in products_within_budget:
    products_above_dict["Name"] += [details[0]]  # Adds name
    products_above_dict["Unit Price"] += [details[1]]  # Adds unit price

print(products_above_dict)  # Prints dictionary for testing purposes

# Prints Product details in a well formatted way
print("\n*** Products above the budget ***\n")
product_frame = pandas.DataFrame(products_above_dict)  # creates data frame

# Changes the index to reference the names rather than an actual index number
product_frame = product_frame.set_index("Name")

# Sorts the data frame in ascending order of the unit prices
product_frame = product_frame.sort_values("Unit Price")

# Formats the unit prices in currency and unit price format
# so that they have $'s and the per unit (e.g. $0.25 per g)
# "currency" is the call to the currency() function above
product_frame["Unit Price"] = product_frame["Unit Price"].apply(currency)

print(product_frame)  # Prints data frame
