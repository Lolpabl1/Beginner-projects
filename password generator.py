import random


# getting minimum length required for the password
def get_min_length_of_password():
    while True:
        min_length_of_password = input(
            "What is the minimum requirement for the length of the password? "
        )
        if min_length_of_password.isdigit():
            min_length_of_password = int(min_length_of_password)
            break
        else:
            print("Please write a number")
            print()
    return min_length_of_password


# getting minimum number of digits required for the password
def get_min_digits():
    while True:
        min_digits = input(
            "What is the minimum requirement for the number of digits for the password? "
        )
        if min_digits.isdigit():
            min_digits = int(min_digits)
            break
        else:
            print("Please write a number")
            print()
    return min_digits


# getting minimum number of special characters required for the password
def get_min_special_characters():
    while True:
        min_special_characters = input(
            "What is the minimum requirement for the number of special characters for the password? "
        )
        if min_special_characters.isdigit():
            min_special_characters = int(min_special_characters)
            break
        else:
            print("Please write a number")
            print()
    return min_special_characters


# getting minimum number of uppercase letters required for the password
def get_min_uppercase_letters():
    while True:
        min_uppercase_letters = input(
            "What is the minimum requirement for the number of uppercase letters for the password? "
        )
        if min_uppercase_letters.isdigit():
            min_uppercase_letters = int(min_uppercase_letters)
            break
        else:
            print("Please write a number")
            print()
    return min_uppercase_letters


# calculating minimum number of lowercase letters required for the password
def get_min_lowercase_letters(
    min_length_of_password, min_digits, min_special_characters, min_uppercase_letters
):
    min_lowercase_letters = min_length_of_password - (
        min_digits + min_special_characters + min_uppercase_letters
    )
    if min_lowercase_letters == 0:
        min_lowercase_letters = 1
    return min_lowercase_letters


def create_password(length, characters):
    password = []
    for _ in range(length):
        code = random.choice(characters)
        password.append(code)
    return password


def generate_password():
    min_length_of_password = get_min_length_of_password()
    min_digits = get_min_digits()
    min_special_characters = get_min_special_characters()
    min_uppercase_letters = get_min_uppercase_letters()
    min_lowercase_letters = get_min_lowercase_letters(
        min_length_of_password,
        min_digits,
        min_special_characters,
        min_uppercase_letters,
    )

    # Define character sets
    possible_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    possible_lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
    possible_special_characters = list("!@#$%^&*-+_=`~|\\/:;'\"<>,.?()[]{}")

    # Create password components
    digits = create_password(min_digits, possible_digits)
    special_characters = create_password(
        min_special_characters, possible_special_characters
    )
    uppercase_letters = create_password(
        min_uppercase_letters, possible_uppercase_letters
    )
    lowercase_letters = create_password(
        min_lowercase_letters, possible_lowercase_letters
    )

    # Combine and shuffle password components
    password = digits + special_characters + uppercase_letters + lowercase_letters
    random.shuffle(password)

    generated_password = "".join(map(str, password))

    print("Generated Password:", generated_password)


generate_password()
