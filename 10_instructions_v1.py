"""Post usability testing 1: Instructions - component 10 (Trial 1)
Uses input statement, while loop, for loop and if and else statements.
"""
valid_answers = [["Y", "Yes"], ["N", "No"]]
repeat = "yes"
error = ""
while repeat == "yes":
    instructions = input("Do you want the instructions? (Y/N): ").title()
    # Checking if answer is valid or invalid
    for answer in valid_answers:
        if instructions in answer[0]:
            if instructions == "Y":
                print("Display instructions...")
                quit()  # quits program when answer is valid
            elif instructions == "N":
                print("Program continues without instructions...")
                quit()

        elif instructions in answer[1]:
            if instructions == "Yes":
                print("Display instructions...")
                quit()
            elif instructions == "No":
                print("Program continues without instructions...")
                quit()
    print("Display error")  # displays error if answer is invalid
