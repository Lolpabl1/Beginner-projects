import random

possible_options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
options_for_x = (1, 2, 3, 4, 5, 6, 7, 8, 9)

x = random.choice(options_for_x)
y = random.choice(possible_options)
z = random.choice(possible_options)

secret_number = (100 * x + 10 * y + z)

print("In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: 'Pico' when your guess has a correct digit in the wrong place, 'Fermi' when your guess has a correct digit in the correct place, and 'Bagels' if your guess has no correct digits. You have 10 tries to guess the secret number.")

lives = 10

while lives > 0:
    guess = input('\nGuess the three-digit number: ')
    print(guess)
    if len(guess) != 3:
        print("Invalid input. Please enter a three-digit number.")
        continue
    if not guess.isdigit():
        print("Invalid input. Please enter a numeric three-digit number.")
        continue
    if int(guess) == secret_number:
        print("Congratulations! You guessed the correct number. Well done!")
        break
    else:
        lives -= 1
        if int(guess[0]) == x or int(guess[1]) == y or int(guess[2]) == z:
            print("Fermi")
        if int(guess[0]) == y or int(guess[0]) == z:
            print("Pico")
        if int(guess[1]) == x or int(guess[1]) == z:
            print("Pico")
        if int(guess[2]) == x or int(guess[2]) == y:
            print("Pico")
        if int(guess[0]) != x and int(guess[0]) != y and int(guess[0]) != z and int(guess[1]) != x and int(guess[1]) != y and int(guess[1]) != z and int(guess[2]) != x and int(guess[2]) != y and int(guess[2]) != z:
            print("Bagel")

if lives == 0:
    print("You couldn't guess the number in 10 tries")
    print("You lose!")
    print("The correct number was " + str(secret_number))
