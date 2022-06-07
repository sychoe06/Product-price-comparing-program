"""Save data in file - Testing 1
I used pandas to write the frames into separate excel files. The files will be
exported in the assessment folder.
"""
import pandas


# Currency formatting function for unit price only
def currency(number):
    return f"${number:,.2f} per {unit}"


# Display product details function (for products within or above budget)
def display_details(products_list, products_dict, within_or_above):
    # If there are no products that are above or within budget...
    if len(products_list) == 0:  # Then tell the user this.
        print(f"\nNo products were {within_or_above} the budget")
    else:
        # Display all products details
        # Adds product details from list into the lists inside the dictionary
        for details in products_list:
            products_dict["Name"] += [details[0]]  # Adds name
            products_dict["Unit Price"] += [details[1]]  # Adds unit price

        # Prints Product details in a well formatted way
        print(f"\n*** Products {within_or_above} the budget ***\n")
        product_frame = pandas.DataFrame(products_dict)  # create data frame

        # Changes index to reference names rather than an actual index number
        product_frame = product_frame.set_index("Name")

        # Sorts the data frame in ascending order of the unit prices
        product_frame = product_frame.sort_values("Unit Price")

        # Formats the unit prices in currency and unit price format
        # so that they have $'s and the per unit (e.g. $0.25 per g)
        # "currency" is the call to the currency() function above
        product_frame["Unit Price"] = \
            product_frame["Unit Price"].apply(currency)

        print(product_frame)  # Prints data frame
        print()
        return product_frame


unit = "g"  # test unit

# Test data
products_within_budget = [["Greggs", 0.04], ["Nescafe", 0.06]]
products_above_budget = [["Moccona", 0.12]]

# Creates separate list for name and unit price for the products within budget
name_list_within = []
unit_price_list_within = []

# Creates separate list for name and unit price for the products above budget
name_list_above = []
unit_price_list_above = []

# Creates the products within budget dictionary with a label and then
# a list for the product details like name and unit price
products_within_dict = {
    "Name": name_list_within,
    "Unit Price": unit_price_list_within
}

# Creates the products above budget dictionary with a label and then
# a list for the product details like name and unit price
products_above_dict = {
    "Name": name_list_above,
    "Unit Price": unit_price_list_above
}

# Display the details of the products within the budget
product_frame_within = display_details(products_within_budget,
                                       products_within_dict, "within")

# Display the details of the products above the budget
product_frame_above = display_details(products_above_budget,
                                      products_above_dict, "above")

# Write each frame to separate csv files
product_frame_within.to_csv("products_within_budget.csv")
product_frame_above.to_csv("products_above_budget.csv")

print("\nNote: To see saved details of products find excel files called\n"
      "products_within_budget.csv and products_above_budget.csv")
