"""Calculate unit price - trial 3
I used "{:.2f}".format() to format my unit price to 2dp after the calculation.
"""
# Using input statements for testing purposes only!
weight = float(input("Enter weight: "))
unit = input("Enter unit: ")
price = float(input("Enter price: "))

# Calculates unit price - prints for testing purposes
unit_price = "{:.2f}".format(price / weight)  # Formats to 2dp
print(f"Unit price: ${unit_price} per {unit}")
