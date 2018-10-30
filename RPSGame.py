from random import randint

# available weapons=> store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5

# make the computer pick one item at random
computer_choice = choices[randint(0, 2)]


# set lives for computer and player
player = 3
computer_choice = 3

player = False

# show the computer's choice in the terminal window
print("computer_choices:", computer_choice)

# set up our loop
while player is False:
	print("============================================")
	print("Player lives:", player_lives, "/5")
	print("computer_lives lives:", computer_lives, "/5")
	print("============================================")
    # set player to True by making a selection
    print("Choose your weapon!")
    input("Rock, Paper or Scissors?")

    print(player, "\n")

    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won. crap!!
            print("You lose! Paper covers Rock")
        else:
            # we win! such winning
            print("You win!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player)
        else:
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player)
        else:
            print("You win!", player, "cuts", computer_choice)
    elif player == "Quit":
        exit()
    else:
        print(" Not a vlaid option..Check your spelling... that's not a valid choice\n")

# reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0, 2)]
