import copy
import random
import sys
import time

import bext

WIDTH, HEIGHT = bext.size()
NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = 0.1
WIDTH -= 1
HEIGHT -= 1

ANT_UP = "^"
ANT_DOWN = "v"
ANT_LEFT = "<"
ANT_RIGHT = ">"

ANT_COLOR = "red"
BLACK_TILE = "black"
WHITE_TILE = "white"

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"


def main():
    bext.fg(ANT_COLOR)
    bext.bg(WHITE_TILE)
    bext.clear()

    board = {"width": WIDTH, "height": HEIGHT}

    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            "x": random.randint(0, WIDTH - 1),
            "y": random.randint(0, HEIGHT - 1),
            "direction": random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)

    changed_tiles = []
    i = 1
    while True:  # Main program loop.
        display_board(board, ants, changed_tiles, i)
        changed_tiles = []
        next_board = copy.copy(board)

        for ant in ants:
            if board.get((ant["x"], ant["y"]), False) == True:
                next_board[(ant["x"], ant["y"])] = False
                # Turn clockwise.
                if ant["direction"] == NORTH:
                    ant["direction"] = EAST
                elif ant["direction"] == EAST:
                    ant["direction"] = SOUTH
                elif ant["direction"] == SOUTH:
                    ant["direction"] = WEST
                elif ant["direction"] == WEST:
                    ant["direction"] = NORTH
            else:
                next_board[(ant["x"], ant["y"])] = True
                # Turn counter-clockwise.
                if ant["direction"] == NORTH:
                    ant["direction"] = WEST
                elif ant["direction"] == WEST:
                    ant["direction"] = SOUTH
                elif ant["direction"] == SOUTH:
                    ant["direction"] = EAST
                elif ant["direction"] == EAST:
                    ant["direction"] = NORTH
            changed_tiles.append((ant["x"], ant["y"]))

            # Move the ant one tile forward.
            if ant["direction"] == NORTH:
                ant["y"] -= 1
            elif ant["direction"] == SOUTH:
                ant["y"] += 1
            elif ant["direction"] == WEST:
                ant["x"] -= 1
            elif ant["direction"] == EAST:
                ant["x"] += 1

            ant["x"] = ant["x"] % WIDTH
            ant["y"] = ant["y"] % HEIGHT

            changed_tiles.append((ant["x"], ant["y"]))

        board = next_board
        i += 1


def display_board(board, ants, changed_tiles, i=1):
    for x, y in changed_tiles:
        bext.goto(x, y)
        if board.get((x, y), False):
            bext.bg(BLACK_TILE)
        else:
            bext.bg(WHITE_TILE)

        ant_is_here = False
        for ant in ants:
            if (x, y) == (ant["x"], ant["y"]):
                ant_is_here = True

                if ant["direction"] == NORTH:
                    print(ANT_UP, end="")
                elif ant["direction"] == SOUTH:
                    print(ANT_DOWN, end="")
                elif ant["direction"] == EAST:
                    print(ANT_LEFT, end="")
                elif ant["direction"] == WEST:
                    print(ANT_RIGHT, end="")
                break
        if not ant_is_here:
            print(" ", end="")

    bext.goto(0, HEIGHT)
    bext.bg(WHITE_TILE)
    print("Press Ctrl-C to quit.", end="")
    sys.stdout.flush()
    time.sleep(PAUSE_AMOUNT)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
