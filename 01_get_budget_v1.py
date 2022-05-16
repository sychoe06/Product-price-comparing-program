"""Get budget - Trial 1
Uses "float" in the input and only floats or integers are accepted.
Loops until valid budget is entered.
"""
budget = -1
while budget < 0:
    budget = float(input("Enter budget: "))
    if budget < 0:  # if the number is negative than prints error
        print("Please enter a positive number! Try again\n")
    else:
        break
print("program continues...")
