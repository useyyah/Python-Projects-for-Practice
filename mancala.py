import sys

PLAYER_1_PITS = ("A", "B", "C", "D", "E", "F")
PLAYER_2_PITS = ("G", "H", "I", "J", "K", "L")

OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                'K': 'E', 'L': 'F'}

NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

PIT_LABELS = "ABCDEF1LKJIHG2"
INITIAL_NUMBER_OF_SEEDS = 4


def get_board():
    s = INITIAL_NUMBER_OF_SEEDS
    return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
            'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


def display_board(board):
    seed_amounts = []
    for pit in "GHIJKL21ABCDEF":
        num_of_seeds_in_the_pit = str(board[pit]).rjust(2)
        seed_amounts.append(num_of_seeds_in_the_pit)

    print("""
    +------+------+--<<<<<-Player 2----+------+------+------+
    2      |G     |H     |I     |J     |K     |L     |      1
           |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
    S      |      |      |      |      |      |      |      S
    T  {}  +------+------+------+------+------+------+  {}  T
    O      |A     |B     |C     |D     |E     |F     |      O
    R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
    E      |      |      |      |      |      |      |      E
    +------+------+------+-Player 1->>>>>-----+------+------+
        """.format(*seed_amounts))


def ask_for_player_move(player_turn, board):
    while True:
        if player_turn == "1":
            print("Player 1, choose move: A-F (or QUIT)")
        elif player_turn == "2":
            print("Player 2, choose move: G-L (or QUIT)")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing.")
            sys.exit()

        if (player_turn == "1" and response not in PLAYER_1_PITS) or (
                player_turn == "2" and response not in PLAYER_2_PITS):
            print("Please select a pit from your side of the board.")
            continue
        if board.get(response) == 0:
            print("Please select a non-empty pit.")
            continue
        return response


def make_move(board, player_turn, pit):
    seeds_to_sow = board[pit]
    board[pit] = 0
    while seeds_to_sow > 0:
        pit = NEXT_PIT[pit]
        if (player_turn == "1" and pit == "2") or (player_turn == "2" and pit == "1"):
            continue
        board[pit] += 1
        seeds_to_sow -= 1

    # If the last seed went into the player's store, they go again.
    if (pit == player_turn == "1") or (pit == player_turn == "2"):
        return player_turn

    # Check if last seed was in an empty pit; take opposite pit's seeds.
    if player_turn == "1" and pit in PLAYER_1_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        board["1"] += board[opposite_pit]
        board[opposite_pit] = 0
    elif player_turn == "2" and pit in PLAYER_2_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        board["2"] += board[opposite_pit]
        board[opposite_pit] = 0

    if player_turn == "1":
        return "2"
    if player_turn == "2":
        return "1"


def check_for_winner(board):
    player_1_total = board["A"] + board["B"] + board["C"]
    player_1_total += board["D"] + board["E"] + board["F"]
    player_2_total = board["G"] + board["H"] + board["I"]
    player_2_total += board["J"] + board["K"] + board["L"]

    if player_1_total == 0:
        board["2"] += player_2_total
        for pit in PLAYER_2_PITS:
            board[pit] = 0
    elif player_2_total == 0:
        board["1"] += player_1_total
        for pit in PLAYER_1_PITS:
            board[pit] = 0
    else:
        return "no winner"

    if board["1"] > board["2"]:
        return "1"
    elif board["2"] > board["1"]:
        return "2"
    else:
        return "tie"


def main():
    print("""
The ancient two-player seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into that pit. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.""")
    input("Press ENTER to begin.")

    game_board = get_board()
    player_turn = "1"

    while True:
        print("\n" * 60)
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        player_turn = make_move(game_board, player_turn, player_move)

        winner = check_for_winner(game_board)
        if winner == "1" or winner == "2":
            display_board(game_board)
            print(f"Player {winner} has won!")
            sys.exit()
        elif winner == "tie":
            display_board(game_board)
            print("There is a tie!")
            sys.exit()


if __name__ == "__main__":
    main()
