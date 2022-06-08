"""Post usability testing 1: Instructions - component 10 (Trial 2)
Uses the function from 09_save_data_in_file_v3 to check if answer to seeing
instructions is yes or no.
"""


# Checking whether answer to question is 'Y' or 'N'
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
    print("")
else:
    print("Program continues without instructions...")
