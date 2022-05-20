"""Based on 03_product_details_v2, (get product details) - Trial 2
To solve the issue of having a messy layout because of too many For loops in
the main routine, I moved all the For loops into a single function. This helps
as it can clear up some space in the main routine making it more simple and
better layout and still produces the same results.
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
    getting_option = "yes"
    while getting_option == "yes":
        response = input(question).lower()
        for option in valid_options:
            if response in option:
                response = option[0].lower()
                return response

        print(error)
        return check_valid(question, valid_options)


# Converts product weight's unit to match main unit
def unit_converter():
    # If unit = kg or kl
    for unit_kil in kilo_units:
        if unit in unit_kil:
            # If main unit = g or L
            for mid in middle_units:
                if main_unit in mid:
                    new_weight = weight * 1000
                    return new_weight
            # If main unit = mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    new_weight = weight * 1000000
                    return new_weight

    # If unit = g or L
    for unit_mid in middle_units:
        if unit in unit_mid:
            # If main unit = kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    new_weight = weight / 1000
                    return new_weight
            # If main unit = mg or ml
            for mil in milli_units:
                if main_unit in mil:
                    new_weight = weight * 1000
                    return new_weight

    # If unit = mg or ml
    for unit_mil in milli_units:
        if unit in unit_mil:
            # If main unit = kg or kl
            for kil in kilo_units:
                if main_unit in kil:
                    new_weight = weight / 1000000
                    return new_weight
            # If main unit = g or L
            for mid in middle_units:
                if main_unit in mid:
                    new_weight = weight / 1000
                    return new_weight
    return weight


# Main routine
# List of all valid units
valid_units = [["kg", "kilograms", "kilogram"],
               ["mg", "milligrams", "milligram"], ["g", "grams", "gram"],
               ["l", "litre", "liter", "litres", "liters"],
               ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]

# Separate list for kg and kl
kilo_units = [["kg", "kilograms", "kilogram"],
              ["kl", "kilolitre", "kiloliter", "kilolitres", "kiloliters"]]

# Separate list for g and L
middle_units = [["g", "grams", "gram"],
                ["l", "litre", "liter", "litres", "liters"]]


# Separate list for mg and ml
milli_units = [["mg", "milligrams", "milligram"],
               ["ml", "millilitre", "milliliter", "millilitres",
                "milliliters"]]

name = ""
main_unit = "kg"  # for testing purposes only
print(f"main unit: {main_unit}")
print("Please enter the following details for the product\n")
while name != "X":
    # Product details
    name = input("Product name or 'X' to finish: ").title()
    if name == "X":
        break
    else:
        weight = number_checker(f"Weight of {name} (without units): ")
        unit = check_valid("The unit for weight: ", valid_units)
        converted = unit_converter()

        # Testing purposes only - to show that conversion has occurred
        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: {converted}{main_unit}\n")

        price = number_checker("Price (without $ sign): ")
        print("-" * 40)
