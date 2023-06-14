import random

#making it a first to three
user_score=0
comp_score=0

while user_score<3 and comp_score<3:
	
	#getting user input
	user_choice=input("ROCK,PAPER OR SCISSORS: ")
	user_choice = user_choice.lower()

	#getting computer input
	possible_options = ["rock","paper","scissors"]
	comp_choice=random.choice (possible_options)

	#defining win condition
	if user_choice == comp_choice:
		print("You chose "+ user_choice + " and the computer chose "+comp_choice)
	elif user_choice =="rock":
		if comp_choice=="paper":
			print("You chose rock and the computer chose paper")
			print("You lose")
			comp_score+=1
		else:
			print("You chose rock and the computer chose scissors")
			print("You win")
			user_score+=1
	elif user_choice =="paper":
		if comp_choice=="scissors":
			print("You chose paper and the computer chose scissors")
			print("You lose")
			comp_score+=1
		else:
			print("You chose paper and the computer chose rock")
			print("You win")
			user_score+=1
	elif user_choice =="scissors":
		if comp_choice=="rock":
			print("You chose scissors and the computer chose rock")
			print("You lose")
			comp_score+=1
		else:
			print("You chose scissors and the computer chose paper")
			print("You win")
			user_score+=1
	else:
		print("Invalid option")
	print("User score: ")
	print(user_score)
	print("Comp score: ")
	print(comp_score)
if user_score ==3:
	print("YOU WIN")
else:
	print("YOU LOSE")