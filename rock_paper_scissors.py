import random
import sys
import time

wins = 0
losses = 0
ties = 0

while True:  # Main game loop.
    while True:
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")
        player_move = input("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit").upper()
        if player_move == "Q":
            print("Thanks for playing!")
            sys.exit()
        if player_move == "R" or player_move == "P" or player_move == "S":
            break
        else:
            print("Type one of R, P, S, or Q.")

    if player_move == "R":
        print("Rock versus...")
        player_move = "ROCK"
    elif player_move == "P":
        print("Paper versus...")
        player_move = "PAPER"
    elif player_move == "S":
        print("Scissors versus...")
        player_move = "SCISSORS"

    time.sleep(0.5)
    print("1...")
    time.sleep(0.25)
    print("2...")
    time.sleep(0.25)
    print("3...")
    time.sleep(0.25)

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "ROCK"
    elif random_number == 2:
        computer_move = "PAPER"
    elif random_number == 3:
        computer_move = "SCISSORS"
    print(computer_move)
    time.sleep(0.5)

    if player_move == computer_move:
        print("It's a tie!")
        ties = ties + 1
    elif player_move == "ROCK" and computer_move == "SCISSORS":
        print("You win!")
        wins = wins + 1
    elif player_move == "PAPER" and computer_move == "ROCK":
        print("You win!")
        wins = wins + 1
    elif player_move == "SCISSORS" and computer_move == "PAPER":
        print("You win!")
        wins = wins + 1
    elif player_move == "ROCK" and computer_move == "PAPER":
        print("You lose!")
        losses = losses + 1
    elif player_move == "PAPER" and computer_move == "SCISSORS":
        print("You lose!")
        losses = losses + 1
    elif player_move == "SCISSORS" and computer_move == "ROCK":
        print("You lose!")
        losses = losses + 1
