import random
import sys

BLANK = ""


def get_board():
    new_board = {}
    for x in range(4):
        for y in range(4):
            new_board[(x, y)] = BLANK

    starting_twos_placed = 0
    while starting_twos_placed < 2:
        random_space = (random.randint(0, 3), random.randint(0, 3))
        if new_board[random_space] == BLANK:
            new_board[random_space] = 2
            starting_twos_placed = starting_twos_placed + 1

    return new_board


def draw_board(board):
    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]
            label_for_tile = str(tile).center(5)
            labels.append(label_for_tile)

    print("""
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    |     |     |     |     |
    |{}|{}|{}|{}|
    |     |     |     |     |
    +-----+-----+-----+-----+
    """.format(*labels))


def get_score(board):
    score = 0
    for x in range(4):
        for y in range(4):
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combine_tiles_in_column(column):
    combined_tiles = []
    for i in range(4):
        if column[i] != BLANK:
            combined_tiles.append(column[i])

    # Add blanks till there are 4 tiles.
    while len(combined_tiles) < 4:
        combined_tiles.append(BLANK)

    # Combine numbers if the one above is the same number.
    for i in range(3):
        if combined_tiles[i] == combined_tiles[i + 1]:
            combined_tiles[i] *= 2
            for above_index in range(i + 1, 3):
                combined_tiles[above_index] = combined_tiles[above_index + 1]
            combined_tiles[3] = BLANK
    return combined_tiles


def make_move(board, move):
    if move == 'W':
        all_columns_spaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                              [(1, 0), (1, 1), (1, 2), (1, 3)],
                              [(2, 0), (2, 1), (2, 2), (2, 3)],
                              [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        all_columns_spaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                              [(0, 1), (1, 1), (2, 1), (3, 1)],
                              [(0, 2), (1, 2), (2, 2), (3, 2)],
                              [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        all_columns_spaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                              [(1, 3), (1, 2), (1, 1), (1, 0)],
                              [(2, 3), (2, 2), (2, 1), (2, 0)],
                              [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        all_columns_spaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                              [(3, 1), (2, 1), (1, 1), (0, 1)],
                              [(3, 2), (2, 2), (1, 2), (0, 2)],
                              [(3, 3), (2, 3), (1, 3), (0, 3)]]

    board_after_move = {}
    for column_spaces in all_columns_spaces:
        first_tile_space = column_spaces[0]
        second_tile_space = column_spaces[1]
        third_tile_space = column_spaces[2]
        fourth_tile_space = column_spaces[3]

        first_tile = board[first_tile_space]
        second_tile = board[second_tile_space]
        third_tile = board[third_tile_space]
        fourth_tile = board[fourth_tile_space]

        column = [first_tile, second_tile, third_tile, fourth_tile]
        combined_tiles_column = combine_tiles_in_column(column)

        board_after_move[first_tile_space] = combined_tiles_column[0]
        board_after_move[second_tile_space] = combined_tiles_column[1]
        board_after_move[third_tile_space] = combined_tiles_column[2]
        board_after_move[fourth_tile_space] = combined_tiles_column[3]
    return board_after_move


def ask_for_player_move():
    print("Enter move: (WASD or quit)")
    while True:
        move = input(" ").upper()
        if move == "Q":
            print("Thanks for playing!")
            sys.exit()

        if move in ("W", "A", "S", "D"):
            return move
        else:
            print("Enter one of 'W', 'A', 'S', 'D', or 'Q'.")


def add_two_to_board(board):
    while True:
        random_space = (random.randint(0, 3), random.randint(0, 3))
        if board[random_space] == BLANK:
            board[random_space] = 2
            return


def is_full(board):
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
    return True


def main():
    input("Press ENTER to begin.")

    game_board = get_board()

    while True:  # Main game loop.
        draw_board(game_board)
        print(f"Score: {get_score(game_board)}")
        player_move = ask_for_player_move()
        game_board = make_move(game_board, player_move)
        add_two_to_board(game_board)

        if is_full(game_board):
            draw_board(game_board)
            print("You lost! Thanks for playing.")
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
