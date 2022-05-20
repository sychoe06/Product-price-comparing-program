"""Added 02_main_unit_v5 to original v2 of this base code
"""
# Import statements

# Functions go here


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
def check_units(question, valid_options):
    error = "Sorry that is not a valid choice\n"
    getting_option = True
    while getting_option is True:
        response = input(question).lower()
        for unit in valid_options:
            if response in unit:
                response = unit[0].lower()
                return response
            else:
                break
        print(error)
    return check_units(question, valid_options)

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
valid_units = [["kg", "kilograms", "kilogram"],
               ["mg", "milligrams", "milligram"], ["g", "grams", "gram"],
               ["l", "litre", "liter", "litres", "liters"],
               ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]

# Ask user if they have used the program before and
# show instructions if necessary

# Repeat component 3-5 until "X" (loop)

    # Get budget
    budget = number_checker("Enter budget: ")

    # Get main unit for products
    main_unit = check_units("Enter main unit for products (e.g. kg, ml etc): ",
                            valid_units)

    # Get product details

    # Calculate unit price

    # Append details to list

# Display all products details (within budget)

# Display all products outside budget

# Recommendation for "best buy"

# Save data in a file
