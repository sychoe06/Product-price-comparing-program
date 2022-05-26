"""Append details to list - testing 1
Checks whether the price that is entered for the product is less than or equal
to the budget or above the budget.
"""
# Temporary input statements - for testing purposes only
budget = float(input("Budget: "))
name = input("Name: ")
price = float(input("Price: "))
if price <= budget:
    print(f"{name} is within the budget")
else:
    print(f"{name} is above the budget")
