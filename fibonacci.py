import sys

while True:
    while True:
        response = input("Input how many Fibonacci number you want to calculate or type 'QUIT' to quit.").upper()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print("Please enter a number greater than 0, or QUIT.")
    print("\n")

    if nth == 1:
        print("0")
        print("\n")
        print("The #1 Fibonacci number is 0.")
        continue
    elif nth == 2:
        print("0, 1")
        print("\n")
        print("The #2 Fibonacci number is 1.")
        continue

    if nth >= 10000:
        print("WARNING: This may take a while! Press Ctrl-C if you want to quit.")
        input("Press ENTER to begin.")

    second_to_last_number = 0
    last_number = 1
    fib_numbers_calculated = 2
    print("0, 1", end="")

    while True:
        next_number = second_to_last_number + last_number
        fib_numbers_calculated += 1
        print(next_number, end="")

        if fib_numbers_calculated == nth:
            print("\n\n")
            print(f"The #{fib_numbers_calculated} Fibonacci number is {next_number}", sep="")
            break

        print(", ", end="")
        second_to_last_number = last_number
        last_number = next_number
