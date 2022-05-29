"""Display products within budget - testing 1
Creates a dictionary for the products within the budget and prints it later
Also prints the product details in a well formatted way using a for loop.
"""
# Test data list
products_within_budget = [["Greggs", 0.04],
                          ["Moccona", 0.12],
                          ["Nescafe", 0.04]]

# Creates the products within budget dictionary with a label and then
# an empty list that will have values added to it later
products_within_dict = {
    "Name": [],
    "Unit Price": []
}

# Adds the product details from list into the empty list in the dictionary
for details in products_within_budget:
    products_within_dict["Name"] += [details[0]]  # Adds name
    products_within_dict["Unit Price"] += [details[1]]  # Adds unit price

print(products_within_dict)  # Prints dictionary for testing purposes

# Prints Product details in a well formatted way
print("\n*** Products within the budget ***\n")
print("Name:    Unit Price:")
for products in products_within_budget:
    print(products[0], " ", products[1])

