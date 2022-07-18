import random
import sys

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
                r"""
                 +--+
                 |  |
                 O  |
                    |
                    |
                    |
                =====""",
                r"""
                 +--+
                 |  |
                 O  |
                 |  |
                    |
                    |
                =====""",
                r"""
                 +--+
                 |  |
                 O  |
                /|  |
                    |
                    |
                =====""",
                r"""
                 +--+
                 |  |
                 O  |
                /|\ |
                    |
                    |
                =====""",
                r"""
                 +--+
                 |  |
                 O  |
                /|\ |
                /   |
                    |
                =====""",
                r"""
                 +--+
                 |  |
                 O  |
                /|\ |
                / \ |
                    |
                ====="""]

CATEGORY = 'Animals'
WORDS = 'ANT BABOON, BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR' \
        'COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK' \
        'LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT' \
        'PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK' \
        'SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE' \
        'WOLF WOMBAT ZEBRA'.split()


def draw_hangman(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print(f"The category is: {CATEGORY}")
    print("\n")

    print("Missed letter: ", end="")
    for letter in missed_letters:
        print(letter, end=" ")
    if len(missed_letters) == 0:
        print("No missed letters.")
    print("\n")

    blanks = ["_"] * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks[i] = secret_word[i]
    print(" ".join(blanks))


def get_player_guess(already_guessed):
    while True:
        guess = input("Guess a letter.").upper()
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in already_guessed:
            print("You have already guessed that already. Please try again.")
        elif not guess.isalpha():
            print("Please enter a letter")
        else:
            return guess


def main():
    missed_letters = []
    correct_letters = []
    secret_word = random.choice(WORDS)

    while True:
        draw_hangman(missed_letters, correct_letters, secret_word)
        guess = get_player_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters.append(guess)

            found_all_letters = True
            for secret_word_letter in secret_word:
                if secret_word_letter not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"You have won! The secret word is {secret_word}")
                break

        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                print(f"You have run out of guesses. The correct word was {secret_word}.")
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
