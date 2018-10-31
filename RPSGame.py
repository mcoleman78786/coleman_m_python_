# import the random packages so that we can generate random numbers
from random import randint

# choices is an array => a container that can hold multiple items
# # arrays are a 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 3

# make the computer choose a weapon from choices at random
computer_choice = choices[randint(0,2)]

computer_choice_lives = 3

# print the choice to the terminal window
#print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
	#set player to True by making a selection
	print("=====================================")
	print("Choose your weapon!")
	player = input("Rock, Paper or Scissors?\n")

	print("Player chooses", player, "\n")
	print("Computer chooses: ", computer_choice)

	if player == computer_choice:
		print("Tie! You live to shoot another day")
		print("Player Score", player_lives,"Computer Score", computer_choice_lives)



	elif player == "Rock":
		if computer_choice == "Paper":
			print("You lose! Paper covers Rock")
			player_lives = player_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)
		
		else:
			print("You win!", player, "smashes", computer_choice)
			computer_choice_lives = computer_choice_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)
			

	elif player == "Paper":
		if computer_choice == "Scissors":
			print("You lose! Scissors cuts Paper")
			player_lives = player_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)
		else:
			print("You win!", player, "covers", computer_choice)
			computer_choice_lives = computer_choice_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)

	elif player == "Scissors":
		if computer_choice == "Rock":
			print("You lose! Rock crushes Scissors")
			player_lives = player_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)
		else:
			print("You win!", player, "cuts", computer_choice)
			computer_choice_lives = computer_choice_lives - 1
			print("Player Score", player_lives,"Computer Score", computer_choice_lives)

	elif player == "quit":
			exit()
	else:
		print("Check your spelling... that's not a valid choice\n")

	if computer_choice_lives < 1:
		print("YOU WIN THE GAME")
		choice = input("Enter 'Yes' to restart or 'No' to exit")
		
		if choice == "Yes":
			player_lives = 3
			computer_choice_lives = 3
			player=False
			computer_choice = choices[randint(0, 2)]

		elif userInput == "No":
			exit()

	if player_lives < 1:
		print("YOU LOSE THE GAME")
		choice = input("Enter 'Yes' to restart or 'No' to exit")
		if choice == "Yes":
			player_lives = 3
			computer_choice_lives = 3
			player=False
			computer_choice = choices[randint(0, 2)]

		elif choice == "No":
			exit()

		
	player = False 
	computer_choice = choices[randint(0, 2)]

