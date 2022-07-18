import random


def ask_for_guess():
    while True:
        guess = input("> ")
        if guess.isdecimal():
            return int(guess)
        print("Please enter a number between 1 and 100.")


guess_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")

for i in range(10):
    print(f"You have {10 - i} guesses left.")
    guess = ask_for_guess()
    if guess == guess_number:
        break

    if guess < guess_number:
        print("Your guess is too low.")
    if guess > guess_number:
        print("Your guess is too high.")

if guess == guess_number:
    print("You won!")
else:
    print("You run out of guesses. You lost!")
