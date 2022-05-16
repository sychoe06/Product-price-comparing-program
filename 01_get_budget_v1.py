"""Get budget - Trial 1
Uses "float" in the input to make sure that only numbers can be entered.
Loops until valid budget is entered.
"""
budget = -1
while budget < 0:
    budget = float(input("Enter budget: "))
    if budget < 0:  # if the number is negative than prints error
        print("Please enter a positive number! Try again")
    else:
        break
print("program continues...")
