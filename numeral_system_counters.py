while True:
    response = input("Enter the starting number > ")
    if response == "":
        response = "0"
        break
    if response.isdecimal():
        break
    print("Please enter a number greater than or equal to 0.")
start = int(response)

while True:
    response = input("Enter how many numbers to display > ")
    if response == "":
        response = "1000"
        break
    if response.isdecimal():
        break
    print("Please enter a number.")
amount = int(response)

for number in range(start, start + amount):
    hex_number = hex(number)[2:].upper()
    bin_number = bin(number)[2:]
    oct_number = oct(number)[2:]
    print(f"DEC: {number}, HEX: {hex_number}, BIN: {bin_number}, OCT: {oct_number}")
