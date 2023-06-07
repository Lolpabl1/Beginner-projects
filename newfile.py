import random
choices=["rock","paper","scissors"]
user_score = 0 
comp_score = 0
while user_score<3 and comp_score <3:
	user_choice=input("ROCK, PAPER OR SCISSORS: ")
	comp_choice=random.choice(choices)
	if user_choice == comp_choice:
		print("You chose "+user_choice+"and the computer chose "+comp_choice)
		print("IT IS A DRAW")
	elif user_choice == "paper":
		if comp_choice=="rock":
			print("You chose paper and the computer chose rock")
			print("YOU WIN")
			user_score+=1
		else:
			print("You chose paper and the computer chose scissors")
			print("YOU LOSE")
			comp_score+=1
	elif user_choice == "rock":
		if comp_choice=="scissors":
			print("You chose rock and the computer chose scissors")
			print("YOU WIN")
			user_score+=1
		else:
			print("You chose rock and the computer chose paper")
			print("YOU LOSE")
			comp_score+=1		
	elif user_choice == "scissors":
		if comp_choice=="paper":
			print("You chose scissors and the computet chose paper")
			print("YOU WIN")
			user_score+=1
		else:
			print("You chose scissors and the computer chose rock")
			print("YOU LOSE")
			comp_score+=1
	else:
		print("INVALID OUTPUT")
	print("user_score: "+str(user_score))
	print("comp_score: "+ str(comp_score))
print("GAME OVER")
