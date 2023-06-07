import random 
words=["Alaska","Arizona","Alabama","Arkansas","Colorado","California","Delaware","Florida","Hawaii","illinois","Idaho","Indiana","Iowa","Kentucky","Kansas","Louisiana","Montana","Minnesota","Michigan","Massachusetts","Maine","Mississippi","Missouri","Maryland","Nevada","New Jersey","New Hampshire","Nebraska","North Dakota","New Mexico","North Calorina","Ohio","Oregon","Georgia","New York","Oklahoma","Washington","Utah","Vermont","South Carolina","Wisconsin","South Dakota","Virginia","West Virginia","Texas","Rhode Island","Tennessee","Wyoming"]
Hangman_pics=['''  
+---+
      |
      |
      |
    === ''', '''
+---+
O   |
      |
      |
    === ''', '''
+---+
O   |
  |   |
      |
    ===''','''
+---+
 O  |
/|   |
      |
    ===''','''
+---+
 O   |
/|\  |
      |
    ===''','''
+---+
 O   |
/|\  |
/    |
    ===''','''
+---+
 O   |
/|\  |
/ \  |
    ===''']
secret_word = random.choice(words).lower().replace(" ", "")
lives = 6
blanks = list("_"*len(secret_word))
print(" ".join(blanks))
while True:
	print(Hangman_pics[6 - lives])
	guess=input("Guess a letter: ")
	if guess in secret_word:
		for i in range(len(secret_word)):
		              if secret_word[i] == guess:
		              	blanks[i] = guess
		print(" ".join(blanks))
	else:
		print("Incorrect guess")
		lives-=1
		print("You have",lives, "lives remaining.")
		if lives ==0:
			print(Hangman_pics[5])
			print("You lost! The word was:",secret_word)
			break
	if "_" not in blanks:
	       print("Congratulations! You guessed the word:", secret_word)
	       break