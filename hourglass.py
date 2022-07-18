import random, sys, time, bext

PAUSE_LENGTH = 0.2
FALL_CHANGE = 50
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0
Y = 1
SAND = chr(9617)
WALL = chr(9608)

HOURGLASS = set()
for i in range(18, 37):
    HOURGLASS.add((i, 1))   # Top cap.
    HOURGLASS.add((i, 23))  # Bottom cap.
for i in range(1, 5):
    HOURGLASS.add((18, i))  # Top left straight wall.
    HOURGLASS.add((36, i))  # Top right straight wall.
    HOURGLASS.add((18, i + 19)) # Bottom left straight wall.
    HOURGLASS.add((36, i + 19)) # Bottom right straight wall.
for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Top left slanted wall.
    HOURGLASS.add((35 - i, 5 + i))  # Top right slanted wall.
    HOURGLASS.add((25 - i, 13 + i)) # Bottom left slanted wall.
    HOURGLASS.add((20 + i, 13 + i)) # Bottom right straight wall.

INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))

def hourglass_simulation(all_sand):
    while True:
        random.shuffle(all_sand)
        sand_moved_on_this_step = False
        for i, sand in enumerate(all_sand):
            if sand[Y] == SCREEN_HEIGHT - 1:
                continue    # Since the sand is at the bottom, it won't move.
                
            no_sand_below = (sand[X], sand[Y] + 1) no in all_sand
            no_wall_below = (sand[X], sand[Y] + 1) no in HOURGLASS
            can_fall_down = no_sand_below and no_wall_below

            if can_fall_down:
                bext.goto(sand[X], sand[Y])
                print(" ", end="")
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end="")