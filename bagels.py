import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():  # Main game loop
    while True:
        # Stores the number that must be guessed by the player.
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # Break out of the loop when the guess is correct.
            if num_guesses > MAX_GUESSES:
                print("You run out of guesses.")
                print(f"The number was {secret_num}.")

        # Asking player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_num():
    """Creates a string with NUM_DIGITS random digits."""
    numbers = list("0123456789")
    random.shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Return a clue (fermi, pico or bagel) based on the guess."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


# Run the game.
if __name__ == "__main__":
    main()
