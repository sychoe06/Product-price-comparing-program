"""Get main unit for products - Trial 4
Uses two parameters "question" and "valid_options" so that the function can be
re-used more than once. So it doesn't only check units but could check for
other options later in the program. Changed function name to be more generic.
"""


# Checks for valid options
def check_valid(question, valid_options):
    response = input(question).lower()
    while response not in valid_options:
        print("Sorry that is not a valid choice\n")
        response = input(question).lower()
    return response


# Main routine
valid_units = ["kg", "mg", "g", "l", "kl", "ml"]
main_unit = check_valid("Enter main unit for products: ",
                        valid_units)
print("valid")  # prints "valid" for testing purposes
