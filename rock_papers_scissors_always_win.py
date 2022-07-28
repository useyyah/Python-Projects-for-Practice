import sys
import time

wins = 0

while True:
    while True:
        print(f"{wins} Wins, 0 Loses, 0 Ties")
        player_move = input("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit").upper()
        if player_move == "Q":
            print("Thanks for playing!")
            sys.exit()

        if player_move == "R" or player_move == "P" or player_move == "S":
            break
        else:
            print("Type one of R, P, S, or Q.")

    if player_move == "R":
        print("ROCK versus...")
    elif player_move == "P":
        print("PAPER versus...")
    elif player_move == "S":
        print("SCISSORS versus...")

    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
    time.sleep(0.25)

    if player_move == "R":
        print("SCISSORS")
    elif player_move == "P":
        print("ROCK")
    elif player_move == "S":
        print("PAPER")

    time.sleep(0.5)

    print("You win!")
    wins = wins + 1
