"""Added 01_get_budget_v4 to original v1 of this base code
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

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Repeat component 3-5 until "X" (loop)

    # Get budget
    budget = number_checker("Enter budget: ")

    # Get main unit for products

    # Get product details

    # Calculate unit price

    # Append details to list

# Display all products details (within budget)

# Display all products outside budget

# Recommendation for "best buy"

# Save data in a file
