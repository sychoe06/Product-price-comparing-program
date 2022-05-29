"""

"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# Set up
name = ""
products_within_budget = []
products_above_budget = []

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

        # Checking if product price is within or above budget
        if price <= budget:
            products_within_budget.append(
                [name, weight, unit, price, unit_price])
        else:
            products_above_budget.append(
                [name, weight, unit, price, unit_price])
