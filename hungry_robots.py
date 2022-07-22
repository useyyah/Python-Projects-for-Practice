import random
import sys

WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100
EMPTY_SPACE = " "
PLAYER = "@"
ROBOT = "R"
DEAD_ROBOT = "X"
WALL = chr(9617)


def get_board():
    board = {"teleports": NUM_TELEPORTS}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Add walls on the edges.
    for x in range(WIDTH):
        board[(x, 0)] = WALL
        board[(x, HEIGHT - 1)] = WALL
    for y in range(HEIGHT):
        board[(0, y)] = WALL
        board[(WIDTH - 1, y)] = WALL

    # Add random walls.
    for i in range(NUM_WALLS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = WALL

    # Add the starting dead robots.
    for i in range(NUM_DEAD_ROBOTS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def get_random_empty_space(board, robots):
    while True:
        random_X = random.randint(1, WIDTH - 2)
        random_Y = random.randint(1, HEIGHT - 2)
        if is_empty(random_X, random_Y, board, robots):
            break
    return random_X, random_Y


def is_empty(x, y, board, robots):
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def add_robots(board):
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = get_random_empty_space(board, robots)
        robots.append((x, y))
    return robots


def display_board(board, robots, player_position):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if board[(x, y)] == WALL:
                print(WALL, end="")
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end="")
            elif (x, y) == player_position:
                print(PLAYER, end="")
            elif (x, y) in robots:
                print(ROBOT, end="")
            else:
                print(EMPTY_SPACE, end="")
        print("\n")


def ask_for_player_move(board, robots, player_position):
    player_X, player_Y = player_position

    q = "Q" if is_empty(player_X - 1, player_Y - 1, board, robots) else " "
    w = "W" if is_empty(player_X, player_Y - 1, board, robots) else " "
    e = "E" if is_empty(player_X + 1, player_Y - 1, board, robots) else " "
    d = "D" if is_empty(player_X + 1, player_Y, board, robots) else " "
    c = "C" if is_empty(player_X + 1, player_Y + 1, board, robots) else " "
    x = "X" if is_empty(player_X, player_Y + 1, board, robots) else " "
    z = "Z" if is_empty(player_X - 1, player_Y + 1, board, robots) else " "
    a = "A" if is_empty(player_X - 1, player_Y, board, robots) else " "
    all_moves = (q + w + e + d + c + x + z + a + "S")

    while True:
        print(f"(T)eleports remaining: {board['teleports']}")
        print(f"({q}) ({w}) ({e})")
        print(f"({a}) (S) ({d})")
        print(f"Enter move or QUIT: ({z}) ({x}) ({c})")

        move = input().upper()
        if move == "QUIT":
            print("Thanks for playing.")
            sys.exit()
        elif move == "T" and board["teleports"] > 0:
            board["teleports"] -= 1
            return get_random_empty_space(board, robots)
        elif move != "" and move in all_moves:
            return {"Q": (player_X - 1, player_Y - 1),
                    "W": (player_X, player_Y - 1),
                    "E": (player_X + 1, player_Y - 1),
                    "D": (player_X + 1, player_Y),
                    "C": (player_X + 1, player_Y + 1),
                    "X": (player_X, player_Y + 1),
                    "Z": (player_X - 1, player_Y + 1),
                    "A": (player_X - 1, player_Y),
                    "S": (player_X, player_Y)}[move]


def move_robots(board, robot_positions, player_position):
    player_X, player_Y = player_position
    next_robot_positions = []

    while len(robot_positions) > 0:
        robot_X, robot_Y = robot_positions[0]

        if robot_X < player_X:
            move_X = 1
        elif robot_X > player_X:
            move_X = -1
        elif robot_X == player_X:
            move_X = 0

        if robot_Y < player_Y:
            move_Y = 1
        elif robot_Y > player_Y:
            move_Y = -1
        elif robot_Y == player_Y:
            move_Y = 0

        if board[(robot_X + move_X, robot_Y + move_Y)] == WALL:
            if board[(robot_X + move_X, robot_Y)] == EMPTY_SPACE:
                move_Y = 0
            elif board[(robot_X, robot_Y + move_Y)] == EMPTY_SPACE:
                move_X = 0
            else:
                move_X = 0
                move_Y = 0
        new_robot_X = robot_X + move_X
        new_robot_Y = robot_Y + move_Y

        if board[(robot_X, robot_Y)] == DEAD_ROBOT or board[(new_robot_X, new_robot_Y)] == DEAD_ROBOT:
            del robot_positions[0]
            continue

        # Check if two robots collides, then delete each robot.
        if (new_robot_X, new_robot_Y) in next_robot_positions:
            board[(new_robot_X, new_robot_Y)] = DEAD_ROBOT
            next_robot_positions.remove((new_robot_X, new_robot_Y))
        else:
            next_robot_positions.append((new_robot_X, new_robot_Y))
        del robot_positions[0]
    return next_robot_positions


def main():
    print(f"""Try to not get caught by the robots.
          You can trick them into crashing into each other.
          You have a teleporter to but it only has {NUM_TELEPORTS} charges.""")
    input("Press ENTER to begin.")

    board = get_board()
    robots = add_robots(board)
    player_position = get_random_empty_space(board, robots)
    while True:  # Main game loop.
        display_board(board, robots, player_position)

        if len(robots) == 0:
            print("You destroyed all the robots and WON!!!")
            sys.exit()

        player_position = ask_for_player_move(board, robots, player_position)
        robots = move_robots(board, robots, player_position)
        for x, y in robots:
            if (x, y) == player_position:
                display_board(board, robots, player_position)
                print("You have been caught by robots!")
                sys.exit()


if __name__ == "__main__":
    main()
