ALL_SPACES = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
X = "X"
O = "O"
BLANK = " "


def get_blank_board():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def get_board_str(board):
    return f"""                     
        {board['1']}|{board['2']}|{board['3']}  1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']}  4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']}  7 8 9"""


def is_valid_space(board, space):
    return space in ALL_SPACES and board[space] == True


def is_winner(board, player):
    b, p = board, player
    return ((b["1"] == b["2"] == b["3"] == p) or
            (b["4"] == b["5"] == b["6"] == p) or
            (b["7"] == b["8"] == b["9"] == p) or
            (b["1"] == b["4"] == b["7"] == p) or
            (b["2"] == b["5"] == b["8"] == p) or
            (b["3"] == b["6"] == b["9"] == p) or
            (b["3"] == b["5"] == b["7"] == p) or
            (b["1"] == b["5"] == b["9"] == p))


def is_board_full(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def update_board(board, space, mark):
    board[space] = mark


def main():
    print("Welcome to Tic-Tac-Toe")
    game_board = get_blank_board()
    current_player, next_player = X, O

    while True:  # Main game loop.
        print(get_board_str(game_board))
        move = None
        while not is_valid_space(game_board, move):
            move = input(f"What is {current_player}'s move? (1-9) ")
        update_board(game_board, move, current_player)

        # Check if the game is over.
        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(f"{current_player} has won the game!")
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print("The game is a tie!")
            break
        current_player, next_player = next_player, current_player
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
