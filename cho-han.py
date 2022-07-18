import random
import sys

JAPANESE_NUMBERS = {1: "ICHI", 2: "NI", 3: "SAN",
                    4: "SHI", 5: "GO", 6: "ROKU"}

purse = 5000
while True:
    pot = input(f"You have {purse} mon. How much do you bet? (or QUIT)")
    while True:
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    bet = input("    CHO (even) or HAN (odd)?").upper()
    while True:
        if bet != "CHO" and bet != "HAN":
            print("Please enter either 'CHO' or 'HAN'.")
            continue
        else:
            break

    print("  ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("   ", dice1, "-", dice2)

    roll_is_even = (dice1 + dice2) % 2 == 0
    if roll_is_even:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"

    player_won = bet == correct_bet

    # Displaying the bet results.
    if player_won:
        print(f"You won! You take {pot} mon.")
        purse = purse + pot
        print(f"The house collects a {pot // 10} mon fee.")
        purse = purse - (pot // 10)
    else:
        purse = purse - pot
        print("You lost!")

    if purse == 0:
        print("You have run out of money! Thanks for playing!")
        sys.exit()
