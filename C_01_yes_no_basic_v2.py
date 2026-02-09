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

#testing loop
while True:
    want_instructions = yes_no("do you want to see the instructions? ")
    print(f"you chose {want_instructions}")

print("we done")