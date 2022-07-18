import copy
import random
import sys
import time

WIDTH = 79
HEIGHT = 20
ALIVE = "0"
DEAD = " "

next_cells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD

while True:
    print("\n" * 50)
    cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")
        print("\n")
    print("Press Ctrl-C to quit.")

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            num_neighbors = 0
            if cells[(left, above)] == ALIVE:
                num_neighbors += 1
            if cells[(x, above)] == ALIVE:
                num_neighbors += 1
            if cells[(right, above)] == ALIVE:
                num_neighbors += 1
            if cells[(left, y)] == ALIVE:
                num_neighbors += 1
            if cells[(right, y)] == ALIVE:
                num_neighbors += 1
            if cells[(left, below)] == ALIVE:
                num_neighbors += 1
            if cells[(x, below)] == ALIVE:
                num_neighbors += 1
            if cells[(right, below)] == ALIVE:
                num_neighbors += 1

            if cells[(x, y)] == ALIVE and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and num_neighbors == 3:
                next_cells[(x, y)] = ALIVE
            else:
                next_cells[(x, y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()
