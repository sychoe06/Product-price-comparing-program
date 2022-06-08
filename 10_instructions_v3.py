"""Post usability testing 1: Instructions - component 10 (developing trial 2)
Formatted and displays the proper instructions for the product price
comparing program. Edited the yes/no function with its previous error message
"""


# Checking whether answer to question is 'Y' or 'N' (slightly edited)
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


# Main routine
instructions = yes_or_no("Do you want the instructions? (Y/N): ")
if instructions == "Y":
    print("\n\t- - - - - Instructions - - - - -"
          "\nThis is a program which compares the unit prices\n"
          "of different products. It will help you be able to\n"
          "decide which product you should buy.\n\n"
          
          "Enter your budget which is the maximum limit of money\n"
          "you are willing to spend (don’t include the $ sign).\n"
          "Then enter the main unit which will convert the units\n"
          "of a product to match the main unit. This will help\n"
          "keep the units of the products all the same.\n\n"
          
          "After that enter the details of your products like...\n"
          "the name, weight, unit and price. Make sure to not\n"
          "include the $ sign for the price. And enter the\n"
          "weight and the unit of the product separately.\n\n"
          
          "Enter 'X' instead of entering the product name.\n"
          "This will display the...\n"
          "\t>> Names of each product\n"
          "\t>> Unit prices of each product\n"
          "\t>> Cheapest unit price\n"
          "\t>> Most expensive unit price\n"
          "\t>> Average unit price\n"
          "\t>> And the Best Buy\n\n"
          
          "The 'best buy' is the recommended product to buy\n"
          "because it has the cheapest unit price and is\n"
          "within your budget range.")
    print("\t", "- " * 15)
