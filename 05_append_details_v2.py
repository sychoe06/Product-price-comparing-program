"""Append details to list - based on 05_append_details_v1 (testing 2)
Appends the details of one product into a list and then prints out list for
testing purposes to show that it was successfully added in.
"""
# Set up lists
product_list = []
unit_list = ["g", "kg", "mg", "L", "kl", "ml"]

# Temporary input statements - for testing purposes only
budget = float(input("Budget: "))

name = input("Product name: ")
product_list.append(name)

weight = float(input("Weight: "))
product_list.append(weight)

unit = input("Unit: ")
if unit not in unit_list:
    print("Please enter a valid unit!")
    unit = input("Unit: ")
product_list.append(unit)

price = float(input("Price: "))
product_list.append(price)

unit_price = "{:.2f}".format(price / weight)  # taken from 04_unit_price_v3
product_list.append(unit_price)

print(product_list)
