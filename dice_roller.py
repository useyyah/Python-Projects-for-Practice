import random
import sys

while True:
    try:
        dice_str = input("> ")
        if dice_str.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        dice_str = dice_str.lower().replace(" ", "")

        d_index = dice_str.find("d")  # Finding the d.
        if d_index == -1:
            raise Exception("Missing the 'd' character.")

        number_of_dice = dice_str[:d_index]  # Finding how many dices to roll.
        if not number_of_dice.isdecimal():
            raise Exception("Missing the number of dice.")
        number_of_dice = int(number_of_dice)

        sign_index = dice_str.find("+")  # Finding the plus or minus sign.
        if sign_index == -1:
            sign_index = dice_str.find("-")

        if sign_index == -1:  # Finding the number of sides.
            number_of_sides = dice_str[d_index + 1:]
        else:
            number_of_sides = dice_str[d_index + 1: sign_index]
        if not number_of_sides.isdecimal():
            raise Exception("Missing the number of sides.")
        number_of_sides = int(number_of_sides)

        if sign_index == -1:  # Finding the modifier amount.
            modifier_amount = 0
        else:
            modifier_amount = int(dice_str[sign_index + 1:])
            if dice_str[sign_index] == "-":
                modifier_amount = -modifier_amount

        # Simulating the dice rolls.
        rolls = []
        for i in range(number_of_dice):
            roll_result = random.randint(1, number_of_sides)
            rolls.append(roll_result)
        print(f"Total: {sum(rolls) + modifier_amount} Each die: ", end="")

        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(", ".join(rolls), end="")

        if modifier_amount != 0:
            modifier_sign = dice_str[sign_index]
            print(f", {modifier_sign}{abs(modifier_amount)}", end="")
        print(")")

    except Exception as exc:
        print("Invalid input!!!")
        print(f"Input was invalid because {str(exc)}.")
        continue
