import random
import sys
import time

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

while True:
    response = input(f"How many snails will race? Max:{MAX_NUM_SNAILS}")
    if response.isdecimal():
        num_snails_racing = int(response)
        if 1 < num_snails_racing <= MAX_NUM_SNAILS:
            break
    print(f"Enter a number between 2 and {MAX_NUM_SNAILS}")

# Enter the names of snails.
snail_names = []
for i in range(1, num_snails_racing):
    while True:
        name = input(f"Enter snail #{str(i)}'s name: ")
        if len(name) == 0:
            print("Please enter a name.")
        elif name in snail_names:
            print("Choose a different name.")
        else:
            break
    snail_names.append(name)

print("\n" * 40)
print("START" + (" " * (FINISH_LINE - len("START")) + "FINISH"))
print('|' + (' ' * (FINISH_LINE - 1) + '|'))
snail_progress = {}
for snail_name in snail_names:
    print(snail_name[:MAX_NAME_LENGTH])
    print("@v")
    snail_progress[snail_name] = 0

time.sleep(1.5)

while True:  # Main game loop.
    for i in range(random.randint(1, num_snails_racing // 2)):
        random_snail_name = random.choice(snail_names)
        snail_progress[random_snail_name] += 1

        if snail_progress[random_snail_name] == FINISH_LINE:
            print(f"{random_snail_name} has won!")
            sys.exit()

    time.sleep(0.5)
    print("\n" * 40)

    print("START" + (" " * (FINISH_LINE - len("START")) + "FINISH"))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    for snail_name in snail_names:
        spaces = snail_progress[snail_name]
        print((" " * spaces) + snail_name[:MAX_NAME_LENGTH])
        print(("." * snail_progress[snail_name]) + "@v")
