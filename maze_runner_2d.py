import os
import sys

WALL = "#"
EMPTY = " "
START = "S"
EXIT = "E"
PLAYER = "@"
BLOCK = chr(9617)


def display_maze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (player_x, player_y):
                print(PLAYER, end="")
            elif (x, y) == (exit_x, exit_y):
                print("X", end="")
            elif maze[(x, y)] == WALL:
                print(BLOCK, end="")
            else:
                print(maze[(x, y)], end="")
    print("\n")


while True:
    file_name = input("Enter the filename of the maze (or LIST or QUIT): ")

    if file_name.upper() == "LIST":
        print(f"Maze files found in {os.getcwd()}")
        for file_in_current_working_folder in os.listdir():
            if file_in_current_working_folder.startswith("maze") and file_in_current_working_folder.endswith(".txt"):
                print("  ", file_in_current_working_folder)
        continue

    if file_name.upper() == "QUIT":
        sys.exit()

    if os.path.exists(file_name):
        break
    print(f"There is no file named {file_name}")

# Load the maze from a file.
maze_file = open(file_name)
maze = {}
lines = maze_file.readlines()
player_x = None
player_y = None
exit_x = None
exit_y = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), f"Invalid character at column{x + 1}, line{y + 1}"
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            player_x, player_y = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exit_x, exit_y = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y
assert player_x != None and player_y != None, "No start in maze file."
assert exit_x != None and exit_y != None, "No exit in maze file."

while True:  # Main game loop.
    display_maze(maze)
    while True:
        print('                                 W')
        move = input("Enter direction or QUIT: ASD").upper()

        if move == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if move not in ["W", "A", "S", "D"]:
            print("Invalid direction. Enter W, A, S, or D.")
            continue

        if move == "W" and maze[(player_x, player_y - 1)] == EMPTY:
            break
        if move == "S" and maze[(player_x, player_y + 1)] == EMPTY:
            break
        if move == "A" and maze[(player_x - 1, player_y)] == EMPTY:
            break
        if move == "D" and maze[(player_x + 1, player_y)] == EMPTY:
            break
        print("You cannot move in that direction.")

    if move == "W":
        while True:
            player_y -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y + 1)] == WALL:
                break
            if maze[(player_x - 1, player_y)] == EMPTY or maze[(player_x + 1, player_y)] == EMPTY:
                break
    if move == "S":
        while True:
            player_y += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y + 1)] == WALL:
                break
            if maze[(player_x - 1, player_y)] == EMPTY or maze[(player_x + 1, player_y)] == EMPTY:
                break
    if move == "A":
        while True:
            player_x -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x - 1, player_y)] == WALL:
                break
            if maze[(player_x, player_y - 1)] == EMPTY or maze[(player_x, player_y + 1)] == EMPTY:
                break
    if move == "D":
        while True:
            player_x += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x + 1, player_y)] == WALL:
                break
            if maze[(player_x, player_y - 1)] == EMPTY or maze[(player_x, player_y + 1)] == EMPTY:
                break

    if (player_x, player_y) == (exit_x, exit_y):
        display_maze(maze)
        print("You have reached the exit!")
        print("Thanks for playing!")
        sys.exit()
