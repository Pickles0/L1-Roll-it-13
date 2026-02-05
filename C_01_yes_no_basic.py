# Ask if the User wants to play
#respond appropriately


while True:
    want_instructions = input("do you want to see the instructions?").lower()
    if want_instructions == "yes" or want_instructions == "y":
        print("You said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("You said no")
        break
    else:
        print("Please enter yes/no")

print("we done")
