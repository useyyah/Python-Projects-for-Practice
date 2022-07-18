import random
import sys

GARBAGE_CHARS = "~!@#$%^&*()_+-={}[]|;:,.<>?/"

with open("sevenletterwords.txt") as word_list_file:
    WORDS = word_list_file.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()


def get_words():
    secret_password = random.choice(WORDS)
    words = [secret_password]

    # Find two words with zero matching letters.
    while len(words) < 3:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    # Find two words with 3 matching letters.
    for i in range(500):
        if len(words) == 5:
            break
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 3:
            words.append(random_word)

    # Find 7 words with at least one matching letter.
    for i in range(500):
        if len(words) == 12:
            break
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) != 0:
            words.append(random_word)

    # Add any random words to get 12 words in total.
    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(blocklist=None):
    if blocklist == None:
        blocklist = []

    while True:
        random_word = random.choice(WORDS)
        if random_word not in blocklist:
            return random_word


def num_matching_letters(word1, word2):
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def get_computer_memory_strings(words):
    lines_with_words = random.sample(range(16 * 2), len(words))
    memory_address = 16 * random.randint(0, 4000)

    computer_memory = []
    next_word = 0
    for line_num in range(16):
        left_half = ""
        right_half = ""
        for i in range(16):
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)

        if line_num in lines_with_words:
            insertion_index = random.randint(0, 9)
            left_half = (left_half[:insertion_index] + words[next_word] + left_half[insertion_index + 7:])
            next_word += 1
        if line_num + 16 in lines_with_words:
            insertion_index = random.randint(0, 9)
            right_half = (right_half[:insertion_index] + words[next_word] + right_half[insertion_index + 7:])
            next_word += 1

        computer_memory.append("0x" + hex(memory_address)[2:].zfill(4)
                               + "  " + left_half + "   "
                               + "0x" + hex(memory_address + (16 * 16))[2:].zfill(4)
                               + "  " + right_half)
        memory_address += 16

    return "\n".join(computer_memory)


def ask_for_player_guess(words, tries):
    while True:
        guess = input(f"Enter password: ({tries} tries remaining)").upper()
        if guess in words:
            return guess
        print("That is not one of the possible passwords listed above.")
        print(f"Try entering {words[0]} or {words[1]}.")


def main():
    input("Press ENTER to begin.")

    game_words = get_words()
    computer_memory = get_computer_memory_strings(game_words)
    secret_password = random.choice(game_words)

    print(computer_memory)
    for tries_remaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries_remaining)
        if player_move == secret_password:
            print("ACCESS GRANTED")
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print(f"Access Denied ({num_matches}/7 correct)")
    print(f"Out of tries. Secret password was {secret_password}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
