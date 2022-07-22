import random
import sys

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

input("Press ENTER to start.")

swap_wins = 0
swap_losses = 0
stay_wins = 0
stay_losses = 0

while True:  # Main loop.
    door_with_car = random.randint(1, 3)

    # Ask the player to pick a door.
    print(ALL_CLOSED)
    while True:
        response = input("Pick a door 1, 2, or 3 (or 'quit' to stop): ").upper()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.eit()
        if response == "1" or response == "2" or response == "3":
            break
    door_pick = int(response)

    # Select which goat door to show to the player.

    while True:
        show_goat_door = random.randint(1, 3)
        if show_goat_door != door_pick and show_goat_door != door_with_car:
            break

    # Show the goat door to the player.
    if show_goat_door == 1:
        print(FIRST_GOAT)
    elif show_goat_door == 2:
        print(SECOND_GOAT)
    elif show_goat_door == 3:
        print(THIRD_GOAT)
    print(f"Door {show_goat_door} contains a goat!")

    # Asking the player if they want to swap.
    while True:
        swap = input("Do you want to swap doors? Y/N ").upper()
        if swap == "Y" or swap == "N":
            break

    # Swapping the player's door.
    if swap == "Y":
        if door_pick == 1 and show_goat_door == 2:
            door_pick = 3
        elif door_pick == 1 and show_goat_door == 3:
            door_pick = 2
        elif door_pick == 2 and show_goat_door == 1:
            door_pick = 3
        elif door_pick == 2 and show_goat_door == 3:
            door_pick = 1
        elif door_pick == 3 and show_goat_door == 1:
            door_pick = 2
        elif door_pick == 3 and show_goat_door == 2:
            door_pick = 1

    # Open all the doors.
    if door_with_car == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif door_with_car == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif door_with_car == 3:
        print(THIRD_CAR_OTHERS_GOAT)
    print(f"Door {door_with_car} has the car!")

    # Recording wins and losses for swapping and not swapping.
    if door_pick == door_with_car:
        print("You won!")
        if swap == "Y":
            swap_wins += 1
        elif swap == "N":
            stay_wins += 1
    else:
        print("Sorry, you lost!")
        if swap == "Y":
            swap_losses += 1
        elif swap == "N":
            stay_losses += 1

    # Calculating success rates for swapping and not swapping.
    total_swaps = swap_wins + swap_losses
    if total_swaps != 0:
        swap_success = round(swap_wins / total_swaps * 100, 1)
    else:
        swap_success = 0

    total_stays = stay_wins + stay_losses
    if total_stays != 0:
        stay_success = round(stay_wins / total_stays * 100, 1)
    else:
        stay_success = 0

    print("\n")
    print("Swapping: ", end="")
    print(f"{swap_wins} wins, {swap_losses} losses, ", end="")
    print(f"success rate {swap_success}%")
    print("Not swapping: ", end="")
    print(f"{stay_wins} wins, {stay_losses} losses, ", end="")
    print(f"success rate: {stay_success}%")
    print("\n")
    input("Press ENTER to repeat the experiment...")
