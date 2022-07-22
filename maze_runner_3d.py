import copy
import os
import sys

WALL = "#"
EMPTY = " "
START = "S"
EXIT = "E"
BLOCK = chr(9617)
NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"


def wall_str_to_wall_dict(wall_str):
    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = character
    wall_dict["height"] = height + 1
    wall_dict["width"] = width + 1
    return wall_dict


EXIT_DICT = {(0, 0): "E", (1, 0): "X", (2, 0): "I",
             (3, 0): "T", "height": 1, "width": 4}

ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())

CLOSED = {}
CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____'''.strip())

CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())

CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())

CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())

CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())

CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())


def display_wall_dict(wall_dict):
    print(BLOCK * (wall_dict["width"] + 2))
    for y in range(wall_dict["height"]):
        print(BLOCK, end="")
        for x in range(wall_dict["width"]):
            wall = wall_dict[(x, y)]
            if wall == ".":
                wall = " "
            print(wall, end="")
        print(BLOCK)
    print(BLOCK * (wall_dict["width"] + 2))


def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    dst_wall_dict = copy.copy(dst_wall_dict)
    for x in range(src_wall_dict["width"]):
        for y in range(src_wall_dict["height"]):
            dst_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
    return dst_wall_dict


def make_wall_dict(maze, player_x, player_y, player_direction, exit_x, exit_y):
    if player_direction == NORTH:
        offsets = (("A", 0, -2), ("B", -1, -1), ("C", 0, 1),
                   ("D", 1, -1), ("E", -1, 0), ("F", 1, 0))
    if player_direction == SOUTH:
        offsets = (("A", 0, -2), ("B", 1, 1), ("C", 0, 1),
                   ("D", -1, 1), ("E", 1, 0), ("F", -1, 0))
    if player_direction == EAST:
        offsets = (("A", 2, 0), ("B", 1, -1), ("C", 1, 0),
                   ("D", 1, 1), ("E", 0, -1), ("F", 0, 1))
    if player_direction == WEST:
        offsets = (("A", -2, 0), ("B", -1, 1), ("C", -1, 0),
                   ("D", -1, -1), ("E", 0, 1), ("F", 0, -1))

    section = {}
    for sec, x_off, y_off in offsets:
        section[sec] = maze.get((player_x + x_off), player_y + y_off, WALL)
        if (player_x + x_off, player_y + y_off) == (exit_x, exit_y):
            section[sec] = EXIT

    wall_dict = copy.copy(ALL_OPEN)
    PASTE_CLOSED_TO = {"A": (6, 4), "B": (4, 3), "C": (3, 1),
                       "D": (10, 3), "E": (0, 0), "F": (12, 0)}
    for sec in "ABCDEF":
        if section[sec] == WALL:
            wall_dict = paste_wall_dict(CLOSED[sec], wall_dict, PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    # Drawing the exit signs.
    if section["C"] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 7, 9)
    if section["E"] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 0, 2)
    if section["F"] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 13, 11)
    return wall_dict


print("Maze Runner 3D by Umut Özgür Seyyah")

while True:
    file_name = input("Enter the filename of the maze (or LIST or QUIT): ")
    if file_name.upper() == "LIST":
        print(f"Maze files found in {os.getcwd()}")
        for file_in_current_folder in os.listdir():
            if file_in_current_folder.startswith("maze") and file_in_current_folder.endswith(".txt"):
                print(" ", file_in_current_folder)
        continue

    if file_name.upper() == "QUIT":
        sys.exit()

    if os.path.exists(file_name):
        break
    print(f"There is no file name {file_name}")

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
        assert character in (WALL, EMPTY, START, EXIT), f"Invalid character at column {x + 1}, line {y + 1}"
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

assert player_x != None and player_y != None, "No start point in file."
assert exit_x != None and exit_y != None, "No exit point in file."
player_direction = NORTH

while True:  # Main game loop.
    display_wall_dict(make_wall_dict(maze, player_x, player_y, player_direction, exit_x, exit_y))

    while True:  # Get user move.
        print(f"Location ({player_x}, {player_y}) Direction: {player_direction}")
        print("                   (W)")
        print("Enter direction: (A) (D) or QUIT.")
        move = input("> ").upper()

        if move == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if move not in ["F", "L", "R", "W", "A", "D"] and not move.startswith("T"):
            print("Please enter one of F, L, or R (or W, A, or D).")
            continue

        if move == "F" or move == "W":
            if player_direction == NORTH and maze[(player_x, player_y - 1)] == EMPTY:
                player_y -= 1
                break
            if player_direction == SOUTH and maze[(player_x, player_y + 1)] == EMPTY:
                player_y += 1
                break
            if player_direction == EAST and maze[(player_x + 1, player_y)] == EMPTY:
                player_x += 1
                break
            if player_direction == WEST and maze[(player_x - 1, player_y)] == EMPTY:
                player_x -= 1
                break
        elif move == "L" or move == "A":
            player_direction = {NORTH: EAST, WEST: SOUTH,
                                SOUTH: EAST, EAST: NORTH}[player_direction]
            break
        elif move == "R" or move == "D":
            player_direction = {NORTH: EAST, EAST: SOUTH,
                                SOUTH: WEST, WEST: NORTH}[player_direction]
            break
        elif move.startswith("T"):
            player_x, player_y = move.split()[1].split(",")
            player_x = int(player_x)
            player_y = int(player_y)
        else:
            print("You cannot move in that direction.")

    if (player_x, player_y) == (exit_x, exit_y):
        print("You have escaped the maze!")
        print("Thanks for playing!")
        sys.exit()
