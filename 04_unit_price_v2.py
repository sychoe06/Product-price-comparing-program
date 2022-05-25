"""Calculate unit price - trial 2
I used "%.2f" % unit price to make sure the unit price is rounded to 2dp and
also adds a zero on the end if necessary.
"""
# Using input statements for testing purposes only!
weight = float(input("Enter weight: "))
unit = input("Enter unit: ")
price = float(input("Enter price: "))

# Calculates unit price - prints for testing purposes
unit_price = "%.2f" % (price / weight)  # Rounds to 2dp and adds 0 if necessary
print(f"Unit price: ${unit_price} per {unit}")
