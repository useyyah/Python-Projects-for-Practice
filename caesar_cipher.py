SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    response = input("Do you want to (e)ncrypt or (d)ecrypt?").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")

while True:
    max_key = len(SYMBOLS) - 1
    response = input(f"Please enter the key (0 to {max_key}) to use.").upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

message = input(f"Enter the message to {mode}.").upper()

translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)
