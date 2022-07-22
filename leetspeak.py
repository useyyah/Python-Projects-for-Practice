import random

def main():
    english = input("Enter your leet message... ")
    print("\n")
    leet_speak = english_to_leet_speak(english)
    print(leet_speak)

def english_to_leet_speak(message):
    char_mapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']}
    leet_speak = ""
    for char in message:
        if char.lower() in char_mapping and random.random() <= 0.7:
            possible_leet_replacements = char_mapping[char.lower()]
            leet_replacement = random.choice(possible_leet_replacements)
            leet_speak = leet_speak + leet_replacement
        else:
            # Don't translate to leetspeak.
            leet_speak = leet_speak + char
    return leet_speak

if __name__ == "__main__":
    main()