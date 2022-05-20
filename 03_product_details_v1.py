"""Get product details - First test
"""


# Checks for valid positive number
def number_checker(question):
    number = -1
    error = "Please enter a positive number! No letters and can't be blank\n"
    while number < 0:
        try:
            number = float(input(question))
            if number < 0:
                print(error)
            else:
                return number
        except ValueError:
            print(error)


# Checks for valid options
def check_valid(question, valid_options):
    error = "Sorry that is not a valid choice\n"
    getting_option = True
    while getting_option is True:
        response = input(question).lower()
        for option in valid_options:
            if response in option:
                response = option[0].lower()
                return response
            else:
                break
        print(error)
    return check_valid(question, valid_options)


# Main routine
print("Please enter the following details for the product!")
name = input("Product name: ").title()
weight = number_checker(f"Weight of {name} (without units): ")
unit = check_valid("The unit for weight": )
