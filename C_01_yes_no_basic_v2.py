# Ask if the User wants to play
#respond appropriately

def yes_no(question):

    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")

#main routine

want_instructions = yes_no("do you want to see the instructions?").lower()
want_coffee = yes_no()
print("we done")
