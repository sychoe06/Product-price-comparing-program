"""Calculate unit price - trial 3
I used ".format()" to format my unit price to 2dp when I have calculated it.
"""
# Using input statements for testing purposes only!
weight = float(input("Enter weight: "))
unit = input("Enter unit: ")
price = float(input("Enter price: "))

# Calculates unit price
unit_price = "{:.2f}".format(price / weight)  # Formats to 2dp
print(f"Unit price: ${unit_price} per {unit}")
