import random


def english_to_spongecase(message):
    print("Enter your message...")
    sponge_text = ""
    use_upper = False

    for character in message:
        if not character.isalpha():
            sponge_text += character
            continue

        if use_upper:
            sponge_text += character.upper()
        else:
            sponge_text += character.lower()

        if random.randint(1, 100) <= 90:
            use_upper = not use_upper

    return sponge_text


def main():
    sponge_text = english_to_spongecase(input(" "))
    print("\n")
    print(sponge_text)


if __name__ == "__main__":
    main()
