"""Based on 03_product_details_v2, (get product details) - Trial 1
In my previous code there were too many For loops when converting the unit to
match the main unit. This made my layout look too messy and cluttered.
So I tried to improve the layout by replacing anything that repeated with
functions (line 39-91). So now there are less For loops (line 134-186).
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


# Checks if the main unit is kg or kl - returns new weight
def main_unit_kilo(num):
    for k in kilo_units:
        if main_unit in k:
            weight_new = weight / num
            return weight_new


# Checks if the main unit is kg or kl - returns if True or False
def true_false_kilo():
    for k in kilo_units:
        if main_unit in k:
            return True
        else:
            return False


# Checks if the main unit is g or L - returns new weight
def main_unit_mid(product_unit):
    for middle in middle_units:
        if main_unit in middle:
            if product_unit == "k":
                weight_kilo = weight * 1000
                return weight_kilo
            elif product_unit == "m":
                weight_milli = weight / 1000
                return weight_milli


# Checks if the main unit is g or L - returns if True or False
def true_false_mid():
    for middle in middle_units:
        if main_unit in middle:
            return True
        else:
            return False


# Checks if the main unit is mg or ml - returns new weight
def main_unit_milli(num):
    for mil in milli_units:
        if main_unit in mil:
            weight_new = weight * num
            return weight_new


# Checks if the main unit is mg or ml - returns if True or False
def true_false_milli():
    for mil in milli_units:
        if main_unit in mil:
            return True
        else:
            return False


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
        new_weight = weight

        # Converts units into the main unit so that the weight are all in the
        # same unit (this will help with comparing products later)

        # If unit = kg or kl
        for unit_kil in kilo_units:
            if unit in unit_kil:
                # If main unit = g or L
                mid = true_false_kilo()
                if mid is True:
                    # Then convert weight to g/L
                    new_weight = main_unit_mid("k")
                # If main unit = mg or ml
                milli = true_false_milli()
                if milli is True:
                    # Then convert weight to mg/ml
                    new_weight = main_unit_milli(1000000)
                # If main unit = kg or kl
                kilo = true_false_kilo()
                if kilo is True:
                    new_weight = weight

        # If unit = g or L
        for unit_mid in middle_units:
            if unit in unit_mid:
                # If main unit = kg or kl
                kilo = true_false_kilo()
                if kilo is True:
                    # Then convert weight to kg/kl
                    new_weight = main_unit_kilo(1000)
                # If main unit = mg or ml
                milli = true_false_milli()
                if milli is True:
                    # Then convert weight to mg/ml
                    new_weight = main_unit_milli(1000)
                # If main unit = g or L
                mid = true_false_mid()
                if mid is True:
                    new_weight = weight

        # If unit = mg or ml
        for unit_mil in milli_units:
            if unit in unit_mil:
                # If main unit = kg or kl
                kilo = true_false_kilo()
                if kilo is True:
                    # Then convert weight to kg/kl
                    new_weight = main_unit_kilo(1000000)
                # If main unit = g or L
                mid = true_false_mid()
                if mid is True:
                    # Then convert weight to g/L
                    new_weight = main_unit_mid("m")
                # If main unit = mg or ml
                milli = true_false_milli()
                if milli is True:
                    new_weight = weight

        # Testing purposes only - to show that conversion has occurred
        print(f"\nProduct weight: {weight}{unit}")
        print(f"Converted to main unit weight: {new_weight}{main_unit}\n")

        price = number_checker("Price (without $ sign): ")
        print("-" * 40)
