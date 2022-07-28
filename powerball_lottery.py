import random

# Let the player enter first five numbers, 1 to 69.
while True:
    response = input("Enter 5 different numbers form 1 to 69, with spaces between each number.")
    numbers = response.split()
    if len(numbers) != 5:
        print("Please enter 5 numbers seperated by spaces.")
        continue

    # Converting strings to integers.
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Please enter numbers.")
        continue

    # Check numbers are between 1 and 69.
    for i in range(5):
        if not 1 <= numbers[i] <= 69:
            print("Please type numbers between 1 and 69, both included.")
            continue

    # Check that numbers are unique.
    if len(set(numbers)) != 5:
        print("Please enter 5 unique numbers.")
        continue
    break

while True:
    response = input("Enter the powerball number form 1 to 26.")

    # Convert the strings into integers.
    try:
        powerball = int(response)
    except ValueError:
        print("Please enter a number.")
        continue

    # Check if the number is between 1 and 26.
    if not 1 <= powerball <= 26:
        print("Powerball must be between 1 and 26, both included.")
        continue
    break

# Enter the number of times the player wants to play.
while True:
    response = input("How many times you want to play? (Max: 1000000)")

    try:
        num_plays = int(response)
    except ValueError:
        print("Please enter a number.")
        continue

    if not 1 <= num_plays <= 1000000:
        print("You can play between 1 and 1000000 times.")
        continue
    break

# Run the simulation.
price = "$" + str(2 * num_plays)
print(f"It costs {price} to play {num_plays} times.")
input("Press ENTER to start.")

possible_numbers = list(range(1, 70))
for i in range(num_plays):
    random.shuffle(possible_numbers)
    winning_numbers = possible_numbers[0:5]
    winning_powerball = random.randint(1, 26)

    print("The winning numbers are: ", end="")
    all_winning_nums = ""
    for i in range(5):
        all_winning_nums += str(winning_numbers[i]) + " "
    all_winning_nums += "and " + str(winning_powerball)
    print(all_winning_nums.ljust(21), end="")

    if set(numbers) == set(winning_numbers) and powerball == winning_powerball:
        print("\n")
        print("You have won the lottery!")
        break
    else:
        print(" You lost!")

print(f"You have wasted {price}")
print("Thanks for playing!")
