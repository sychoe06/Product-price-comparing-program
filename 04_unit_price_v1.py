"""Calculate unit price - trial 1
I made a variable called "unit price" to calculate the unit price by dividing
price by weight. I used "round" to round the unit price to 2dp.
"""
# Using input statements for testing purposes only!
weight = float(input("Enter weight: "))
unit = input("Enter unit: ")
price = float(input("Enter price: "))

# Calculates unit price - prints for testing purposes
unit_price = round(price / weight, 2)  # Rounds to 2dp
print(f"Unit price: ${unit_price} per {unit}")
