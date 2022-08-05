LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt_message(message, key):
    return translate_message(message, key, "encrypt")


def decrypt_message(message, key):
    return translate_message(message, key, "decrypt")


def translate_message(message, key, mode):
    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[key_index])
            elif mode == "decrypt":
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)

    return "".join(translated)


def main():
    while True:
        response = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if response.startswith("e"):
            mode = "encrypt"
            break
        elif response.startswith("d"):
            mode = "decrypt"
            break
        print("Please enter the letter e or d.")

    while True:
        response = input("Please specify the key to use. ").upper()
        if response.isalpha():
            key = response
            break

    message = input(f"Enter the message to {mode}: ")

    if mode == "encrypt":
        translated = encrypt_message(message, key)
    elif mode == "decrypt":
        translated = decrypt_message(message, key)

    print(f"{mode.title()}ed message: ")
    print(translated)


if __name__ == "__main__":
    main()
