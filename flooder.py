import bext
import random
import sys

BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

# Constants for shapes and colors.
HEART = chr(9829)
DIAMOND = chr(9830)
SPADE = chr(9824)
CLUB = chr(9827)
BALL = chr(9679)
TRIANGLE = chr(9650)

BLOCK = chr(9608)
LEFT_RIGHT = chr(9472)
UP_DOWN = chr(9474)
DOWN_RIGHT = chr(9484)
DOWN_LEFT = chr(9488)
UP_RIGHT = chr(9492)
UP_LEFT = chr(9496)

TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: "red", 1: "green", 2: "blue",
              3: "yellow", 4: "cyan", 5: "purple"}
COLORS_MODE = "color mode"
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = "shape mode"


def get_board():
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def display_board(board, display_mode):
    bext.fg("white")
    # Displaying the top edge of the board.
    print(DOWN_RIGHT + (LEFT_RIGHT * BOARD_WIDTH) + DOWN_LEFT)

    # Display each row.
    for y in range(BOARD_HEIGHT):
        bext.fg("white")
        if y == 0:
            print(">", end="")
        else:
            print(UP_DOWN, end="")

        # Display each tile in this row.
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if display_mode == COLORS_MODE:
                print(BLOCK, end="")
            elif display_mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end="")

        bext.fg("white")
        print(UP_DOWN)
    # Displaying the bottom edge of the board.
    print(UP_RIGHT + (LEFT_RIGHT * BOARD_WIDTH) + UP_LEFT)


def ask_for_player_move(display_mode):
    while True:
        bext.fg("white")
        print("Choose one of ", end="")

        if display_mode == COLORS_MODE:
            bext.fg("red")
            print("(R)ed ", end="")
            bext.fg("green")
            print("(G)reen ", end="")
            bext.fg("blue")
            print("(B)lue ", end="")
            bext.fg("yellow")
            print("(Y)ellow ", end="")
            bext.fg("cyan")
            print("(C)yan ", end="")
            bext.fg("purple")
            print("(P)urple ", end="")
        elif display_mode == SHAPE_MODE:
            bext.fg("red")
            print("(H)eart ", end="")
            bext.fg("green")
            print("(T)riangle ", end="")
            bext.fg("blue")
            print("(D)iamond ", end="")
            bext.fg("yellow")
            print("(B)all ", end="")
            bext.fg("cyan")
            print("(C)lub ", end="")
            bext.fg("purple")
            print("(S)pade ", end="")
        bext.fg("white")
        response = input("or QUIT:").upper()
        if response == "QUIT":
            sys.exit()
        if display_mode == COLORS_MODE and response in tuple("RGBYCP"):
            return {"R": 0, "G": 1, "B": 2,
                    "Y": 3, "C": 4, "P": 5}[response]
        if display_mode == SHAPE_MODE and response in tuple("HTDBCS"):
            return {"H": 0, "T": 1, "D": 2,
                    "B": 3, "C": 4, "S": 5}[response]


def change_tile(tile_type, board, x, y, char_to_change=None):
    if x == 0 and y == 0:
        char_to_change = board[(x, y)]
        if tile_type == char_to_change:
            return

    board[(x, y)] = tile_type

    if x > 0 and board[(x - 1, y)] == char_to_change:
        change_tile(tile_type, board, x - 1, y, char_to_change)
    if y > 0 and board[(x, y - 1)] == char_to_change:
        change_tile(tile_type, board, x, y - 1, char_to_change)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == char_to_change:
        change_tile(tile_type, board, x + 1, y, char_to_change)
    if y > BOARD_HEIGHT - 1 and board[(x, y + 1)] == char_to_change:
        change_tile(tile_type, board, x, y + 1, char_to_change)


def win_condition(board):
    tile = board[(0, 0)]
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


def main():
    bext.bg("black")
    bext.fg("white")
    bext.clear()

    response = input("Do you want to play in colorbling mode? Y/N")
    if response.upper().startswith("Y"):
        display_mode = SHAPE_MODE
    else:
        display_mode = COLORS_MODE

    game_board = get_board()
    moves_left = MOVES_PER_GAME

    while True:  # Main game loop.
        display_board(game_board, display_mode)
        print(f"Moves left: {moves_left}")
        player_move = ask_for_player_move(display_mode)
        change_tile(player_move, game_board, 0, 0)
        moves_left -= 1

        if win_condition(game_board):
            display_board(game_board, display_mode)
            print("You have won!")
            break
        elif moves_left == 0:
            display_board(game_board, display_mode)
            print("You have run out of moves. You lost!")
            break


if __name__ == "__main__":
    main()
