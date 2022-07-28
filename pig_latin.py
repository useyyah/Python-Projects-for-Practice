VOWELS = ("a", "e", "i", "o", "u", "y")


def english_to_pig_latin(message):
    pig_latin = ""
    for word in message.split():
        prefix_non_letters = ""
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin = pig_latin + prefix_non_letters + " "
            continue

        suffix_non_letters = ""
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()

        prefix_consonants = ""
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        # Adding the pig Latin to the word.
        if prefix_consonants != "":
            word += prefix_consonants + "ay"
        else:
            word += "yay"

        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        pig_latin += prefix_non_letters + word + suffix_non_letters + " "
    return pig_latin


def main():
    print("Pig Latin")
    print("Enter you message: ")
    pig_latin = english_to_pig_latin(input("> "))
    print(pig_latin)


if __name__ == "__main__":
    main()
