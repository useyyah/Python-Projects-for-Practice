import sys

print("Water Bucket Puzzle")

GOAL = 4
steps = 0
water_in_bucket = {"8": 0, "5": 0, "3": 0}

while True:  # Main game loop.
    print("\n")
    print(f"Try to get {str(GOAL)}L of water into one of the buckets:")
    water_display = []

    # Get the strings for the 8L bucket.
    for i in range(1, 9):
        if water_in_bucket["8"] < i:
            water_display.append("      ")
        else:
            water_display.append("WWWWWW")

    # Get the strings for the 5L bucket.
    for i in range(1, 6):
        if water_in_bucket["5"] < i:
            water_display.append("      ")
        else:
            water_display.append("WWWWWW")

    # Get the strings for the 3L bucket.
    for i in range(1, 4):
        if water_in_bucket["3"] < i:
            water_display.append("      ")
        else:
            water_display.append("WWWWWW")

    print('''
    8|{7}|
    7|{6}|
    6|{5}|
    5|{4}|  5|{12}|
    4|{3}|  4|{11}|
    3|{2}|  3|{10}|  3|{15}|
    2|{1}|  2|{9}|  2|{14}|
    1|{0}|  1|{8}|  1|{13}|
     +------+   +------+   +------+
        8L         5L         3L
    '''.format(*water_display))

    for water_amount in water_in_bucket.values():
        if water_amount == GOAL:
            print(f"You have solved the puzzle in {steps} steps!")
            sys.exit()

    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:
        move = input(" ").upper()
        if move == "QUIT" or move == "Q":
            print("Thanks for playing!")
            sys.exit()
        if move in ("F", "E", "P"):
            break
        print("Enter F, E, P, or Q.")

    # Let the player select a bucket.
    while True:
        selected_bucket = input("Select a bucket 8, 5, 3, or QUIT.").upper()

        if selected_bucket == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if selected_bucket in ("8", "5", "3"):
            break

    # Carrying out the selected action.
    if move == "F":
        bucket_size = int(selected_bucket)
        water_in_bucket[selected_bucket] = bucket_size
        steps += 1
    elif move == "E":
        water_in_bucket[selected_bucket] = 0
        steps += 1
    elif move == "P":
        while True:
            print("Select a bucket to pour into: 8, 5, or 3")
            second_bucket = input(" ").upper()
            if second_bucket in ("8", "5", "3"):
                break

        second_bucket_size = int(second_bucket)
        empty_space_in_second_bucket = second_bucket_size - water_in_bucket[second_bucket]
        water_in_bucket = water_in_bucket[selected_bucket]
        amount_to_pour = min(empty_space_in_second_bucket, water_in_bucket)

        water_in_bucket[selected_bucket] -= amount_to_pour

        water_in_bucket[second_bucket] += amount_to_pour
        steps += 1

    elif move == "C":
        pass
