"""Save data in file - based on 09_save_data_in_file_v2 (testing 3)
Made a generic Yes/No function for yes/no questions. This is for the input
statement that is asking the users whether or not they want to save the product
details in separate excel files. This means that I can also allow different
variations of answers like “y”, “yes”, “n” and “no”.
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


# Checking whether answer to question is 'Y' or 'N'
def yes_or_no(question):
    error = "Error! Please enter 'Y' or 'N' to answer this question\n"
    valid_answers = [["Y", "Yes"], ["N", "No"]]  # valid answers list
    valid = False
    while valid is False:  # assuming that answer is not valid
        answer = input(question).title()
        for answer_list in valid_answers:
            if answer in answer_list:  # if answer is in valid_answers list
                return answer_list[0]  # returns 'Y' or 'N'
        print(error)  # print error if answer is not valid


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

save_data = yes_or_no("Save products details in excel files? (Y/N): ")
if save_data == "Y":
    # Write each frame to separate csv files
    product_frame_within.to_csv("products_within_budget.csv")
    product_frame_above.to_csv("products_above_budget.csv")

    print("\nProducts details have been saved to excel files!\n")
    print("Note: To see saved details of products find excel files called\n"
          "products_within_budget.csv and products_above_budget.csv")
else:
    print("\nProducts details have NOT been saved to excel files!")
