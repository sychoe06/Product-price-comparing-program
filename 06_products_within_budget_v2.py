"""Display products within budget - based on 06_products_within_budget_v1
Creates a data frame using 'pandas' for the products within the budget.
This helps to present the details of the products (name and unit price) more
tidily.
"""
import pandas

# Creates separate list for name and unit price for the products
name_list = []
unit_price_list = []

# Test data list
products_within_budget = [["Greggs", 0.04],
                          ["Moccona", 0.12],
                          ["Nescafe", 0.04]]

# Creates the products within budget dictionary with a label and then
# a list for the product details like name and unit price
products_within_dict = {
    "Name": name_list,
    "Unit Price": unit_price_list
}

# Adds the product details from list into the lists inside the dictionary
for details in products_within_budget:
    products_within_dict["Name"] += [details[0]]  # Adds name
    products_within_dict["Unit Price"] += [details[1]]  # Adds unit price

print(products_within_dict)  # Prints dictionary for testing purposes

# Prints Product details in a well formatted way
print("\n*** Products within the budget ***\n")
product_frame = pandas.DataFrame(products_within_dict)  # creates data frame
# Changes the index to reference the names rather than an actual index number
product_frame = product_frame.set_index("Name")
print(product_frame)
