UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

while True:
    message = input("Enter a message to encrypt/decrypt (or QUIT): ")

    if message.upper() == "QUIT":
        break

    translated = ""
    for character in message:
        if character.isupper():
            trans_char_index = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[trans_char_index]
        elif character.islower():
            trans_char_index = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[trans_char_index]

    print("The translated message is: ")
    print(translated)
    print("\n")
