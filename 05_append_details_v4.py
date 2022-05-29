"""Append details to list - based on 05_append_details_v3
Combined 05_append_details_v1 and 05_append_details_v3 together to check if
price is above or within budget and then appends name and unit price to list.
"""
# Set up
name = ""
products_within_budget = []
products_above_budget = []
unit_list = ["g", "kg", "mg", "L", "kl", "ml"]

# Temporary input statements - for testing purposes only
budget = float(input("Budget: "))
while name != "X":  # Temp while loop
    name = input("\nName: ")
    if name == "X":
        break
    else:
        weight = float(input("Weight: "))
        unit = input("Unit: ")
        price = float(input("Price: "))

        # unit_price code taken from 04_unit_price_v3
        unit_price = "{:.2f}".format(price / weight)

        # Checking if product price is within or above budget
        if price <= budget:
            products_within_budget.append(
                [name, unit_price])
        else:
            products_above_budget.append(
                [name, unit_price])

# Printing out lists - testing purposes only
print(f"Products within budget:\n{products_within_budget}\n")
print(f"Products above budget:\n{products_above_budget}")
