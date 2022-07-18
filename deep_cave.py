import random
import sys
import time

WIDTH = 70
PAUSE_AMOUNT = 0.05
left_width = 20
gap_width = 10

time.sleep(2)

while True:
    right_width = WIDTH - gap_width - left_width
    print(("#" * left_width) + (" " * gap_width) + ("#" * right_width))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        left_width = left_width + 1
    else:
        pass

    dice_roll = random.randint(1, 6)

    if dice_roll == 1 and gap_width > 1:
        gap_width = gap_width - 1
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        gap_width = gap_width + 1
    else:
        pass
