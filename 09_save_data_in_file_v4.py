"""Save data in file - Trialling (trial 2)
I used the same function called "check_valid" which is a generic function
that checks for a valid answer from 03_product_details_v5. I tried to make it
work for the yes / no question input statement of this component. Shortened
the input variable "save_data" to "save". And took out the yes/no valid answers
list outside of the function.
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

        # does not print for testing purposes only
        # print(f"\n*** Products {within_or_above} the budget ***\n")
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

        # print(product_frame)  # doesn't print data frame - for testing only
        return product_frame


# Checks for valid options (taken from 03_product_details_v5)
def check_valid(question, valid_options):
    error = "Sorry that is not a valid answer\n"
    getting_option = "yes"
    while getting_option == "yes":
        response = input(question).lower()
        for option in valid_options:
            if response in option:  # if answer is in valid_answers list
                return option[0]
        print(error)


unit = "g"  # test unit

# Test data
products_within_budget = [["Greggs", 0.04], ["Nescafe", 0.06]]
products_above_budget = [["Moccona", 0.12]]

yes_no = [["y", "yes"], ["n", "no"]]  # valid answers list

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

# Ask if user wants to save data to files
save = check_valid("Save products details in excel files? (Y/N): ", yes_no)
if save == "y":
    # Write each frame to separate csv files
    product_frame_within.to_csv("products_within_budget.csv")
    product_frame_above.to_csv("products_above_budget.csv")

    print("\nProducts details have been saved to excel files!\n")
    print("Note: To see saved details of products find excel files called\n"
          "products_within_budget.csv and products_above_budget.csv")
else:
    print("\nProducts details have NOT been saved to excel files!")
