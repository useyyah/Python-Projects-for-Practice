import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def check_key(key):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        print("There is an error in the key or symbol set.")
        return False
    return True


def encrypt_message(message, key):
    return translate_message(message, key, "encrypt")


def decrypt_message(message, key):
    return translate_message(message, key, "decrypt")


def translate_message(message, key, mode):
    translated = ""
    chars_A = LETTERS
    chars_B = key
    if mode == "decrypt":
        chars_A, chars_B = chars_B, chars_A

    for symbol in message:
        if symbol.upper() in chars_A:
            sym_index = chars_A.find(symbol.upper())
            if symbol.isupper():
                translated += chars_B[sym_index].upper()
            else:
                translated += chars_B[sym_index].lower()
        else:
            translated += symbol
    return translated


def generate_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return "".join(key)


def main():
    while True:
        response = input("Do you want to (e)ncrypt or (d)ecrypt?").lower()
        if response.startswith("e"):
            mode = "encrypt"
            break
        elif response.startswith("d"):
            mode = "decrypt"
            break
        print("Please enter letter e or d.")

    while True:
        print("Please specify the key to use.")
        if mode == "encrypt":
            print("Or enter RANDOM to have one generated for you.")
        response = input().upper()
        if response == "RANDOM":
            key = generate_random_key()
            print(f"The key is {key}.")
            break
        else:
            if check_key(response):
                key = response
                break

    message = input(f"Enter the message to {mode}.")

    if mode == "encrypt":
        translated = encrypt_message(message, key)
    elif mode == "decrypt":
        translated = decrypt_message(message, key)

    print(f"The {mode}ed message is: ")
    print(translated)


if __name__ == "__main__":
    main()
