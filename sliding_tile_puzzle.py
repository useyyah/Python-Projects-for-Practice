import random
import sys

BLANK = "  "


def get_board():
    return [["1", "5", "9", "13"], ["2", "6", "10", "14"],
            ["3", "7", "11", "13"], ["4", "8", "12", BLANK]]


def display_board(board):
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    board_to_draw = """
    +------+------+------+------+   
    |      |      |      |      |    
    |  {}  |  {}  |  {}  |  {}  |    
    |      |      |      |      |    
    +------+------+------+------+    
    |      |      |      |      |    
    |  {}  |  {}  |  {}  |  {}  |    
    |      |      |      |      |    
    +------+------+------+------+    
    |      |      |      |      |    
    |  {}  |  {}  |  {}  |  {}  |    
    |      |      |      |      |    
    +------+------+------+------+    
    |      |      |      |      |    
    |  {}  |  {}  |  {}  |  {}  |    
    |      |      |      |      |    
    +------+------+------+------+    
    """.format(*labels)
    print(board_to_draw)


def find_black_space(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == "  ":
                return (x, y)


def ask_for_player_move(board):
    blank_x, blank_y = find_black_space(board)

    w = "W" if blank_y != 3 else " "
    a = "A" if blank_x != 3 else " "
    s = "S" if blank_y != 0 else " "
    d = "D" if blank_x != 0 else " "

    while True:
        print(f"                            ({w})")
        print(f"Enter WASD (or QUIT): ({a}) ({a}) ({d})")

        response = input(" ").upper()
        if response == "QUIT":
            sys.exit()
        if response in (w + a + s + d).replace(" ", ""):
            return response


def make_move(board, move):
    blank_x, blank_y = find_black_space(board)

    if move == "W":
        board[blank_x][blank_y], board[blank_x][blank_y + 1] = board[blank_x][blank_y + 1], board[blank_x][blank_y]
    if move == "A":
        board[blank_x][blank_y], board[blank_x + 1][blank_y] = board[blank_x + 1][blank_y], board[blank_x][blank_y]
    if move == "S":
        board[blank_x][blank_y], board[blank_x][blank_y - 1] = board[blank_x][blank_y - 1], board[blank_x][blank_y]
    if move == "D":
        board[blank_x][blank_y], board[blank_x - 1][blank_y] = board[blank_x - 1][blank_y], board[blank_x][blank_y]


def make_random_move(board):
    blank_x, blank_y = find_black_space(board)
    valid_moves = []

    if blank_y != 3:
        valid_moves.append("W")
    if blank_x != 3:
        valid_moves.append("A")
    if blank_y != 0:
        valid_moves.append("S")
    if blank_x != 0:
        valid_moves.append("D")

    make_move(board, random.choice(valid_moves))


def get_new_puzzle(moves=200):
    board = get_board()

    for i in range(moves):
        make_random_move(board)
    return board


def main():
    input("Press ENTER to begin.")
    game_board = get_new_puzzle()

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(game_board)
        make_move(game_board, player_move)

        if game_board == get_board():
            print("You won!")
            sys.exit()


if __name__ == "__main__":
    main()
