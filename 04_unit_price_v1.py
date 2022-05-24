"""Calculate unit price - trial 1
Calculates the unit price of each product after their product details are
entered. This is done by dividing price by weight.
"""
# Using input statements for testing purposes only!
weight = float(input("Enter weight: "))
unit = input("Enter unit: ")
price = float(input("Enter price: "))
price = price * 100  # Converts the price into cents
unit_price = price / weight
print(f"Unit price: ${unit_price} per {unit}")
