import sys

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH


def get_board():
    board = {}
    for col_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT):
            board[(col_index, row_index)] = EMPTY_SPACE
    return board


def display_board(board):
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for col_index in range(BOARD_WIDTH):
            tile_chars.append(board[(col_index, row_index)])

    print("""
        1234567
       +-------+
       |{}{}{}{}{}{}{}|
       |{}{}{}{}{}{}{}|
       |{}{}{}{}{}{}{}|
       |{}{}{}{}{}{}{}|
       |{}{}{}{}{}{}{}|
       |{}{}{}{}{}{}{}|
       +-------+""".format(*tile_chars))


def ask_for_player_move(player_tile, board):
    while True:
        response = input(f"Player {player_tile}, enter a column or QUIT.").upper().strip()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if response not in COLUMN_LABELS:
            print(f"Enter a number from 1 to {BOARD_WIDTH}.")
            continue

        col_index = int(response) - 1
        if board[(col_index, 0)] != EMPTY_SPACE:
            print("That column is full, please select another one.")
            continue

        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(col_index, row_index)] == EMPTY_SPACE:
                return (col_index, row_index)


def is_full(board):
    for row_index in range(BOARD_HEIGHT):
        for col_index in range(BOARD_WIDTH):
            if board[(col_index, row_index)] == EMPTY_SPACE:
                return False
    return True


def is_winner(player_tile, board):
    # For horizontal four in a row.
    for col_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            tile1 = board[(col_index, row_index)]
            tile2 = board[(col_index + 1, row_index)]
            tile3 = board[(col_index + 2, row_index)]
            tile4 = board[(col_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    # Vertical four in a row.
    for col_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            tile1 = board[(col_index, row_index)]
            tile2 = board[(col_index, row_index + 1)]
            tile3 = board[(col_index, row_index + 2)]
            tile4 = board[(col_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    # Right-down diagonal
    for col_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            tile1 = board[(col_index, row_index)]
            tile2 = board[(col_index + 1, row_index + 1)]
            tile3 = board[(col_index + 2, row_index + 2)]
            tile4 = board[(col_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

            # Left-down diagonal.
            tile1 = board[(col_index + 3, row_index)]
            tile2 = board[(col_index + 2, row_index + 1)]
            tile3 = board[(col_index + 1, row_index + 2)]
            tile4 = board[(col_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    return False


def main():
    game_board = get_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if is_winner(player_turn, game_board):
            display_board(game_board)
            print(f"Player {player_turn} has won!")
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print("There is a tie!")
            sys.exit()

        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn == PLAYER_X


if __name__ == "__main__":
    main()
