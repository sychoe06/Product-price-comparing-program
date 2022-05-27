"""Append details to list - based on 05_append_details_v2
Appends details into list as a list at the same time instead of doing it
individually. Used a while loop to ask for more than one product.
"""
# Set up
name = ""
product_list = []
unit_list = ["g", "kg", "mg", "L", "kl", "ml"]

# Temporary input statements - for testing purposes only
budget = float(input("Budget: "))
while name != "X":  # Temp while loop
    name = input("\nProduct name: ")
    if name == "X":
        break
    else:
        weight = float(input("Weight: "))
        unit = input("Unit: ")
        price = float(input("Price: "))

        # unit_price code taken from 04_unit_price_v3
        unit_price = "{:.2f}".format(price / weight)
        product_list.append([name, weight, unit, price, unit_price])
print(product_list)
