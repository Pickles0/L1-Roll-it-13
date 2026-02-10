def int_check():
    """checks users enter an integer more / equal to 13"""

    error = "Please enter a Integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal? "))

            if game_goal < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

#Main routine starts here
game_goal = int_check()
print(game_goal)