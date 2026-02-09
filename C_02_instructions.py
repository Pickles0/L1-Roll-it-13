# Ask if the User wants to play
#respond appropriately

def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
                return "yes"
        elif response == "no" or response == "n":
                return "no"
        else:
                print("Please enter yes/no")


def instructions():
    """Prints instructions"""


    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


#main routine

# ask the user if the want instructions (check if the say yes or no)
want_instructions = yes_no("do you want to see the instructions? ")

# Display the instructions if the user want to see them
if want_instructions == "yes":
    instructions()

print()
print("program continues")