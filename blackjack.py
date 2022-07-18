import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"


def get_bet(max_bet):  # Asks the player how much they want to bet.
    while True:
        bet = input(f"How much do you bet? (1-{max_bet} or QUIT)").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print("\n")
    if show_dealer_hand:
        print(f"DEALER: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("DEALER: ???")
        display_cards([BACKSIDE] + dealer_hand[1:])
    # Show player's cards.
    print(f"PLAYER: {get_hand_value(player_hand)}")
    display_cards(player_hand)


def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_aces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += "|## |"
            rows[2] += "|###|"
            rows[3] += "| ##|"
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} |"
            rows[2] += f"| {suit} |"
            rows[3] += f"|_{rank.rjust(2, '_')}|"

    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:
        moves = ["(H)it", "(S)tand"]

        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")

        move_prompt = ", ".join(moves)
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D":
            return move


def main():
    money = 5000
    while True:
        if money <= 0:
            print("You are broke!")
            print("Thanks for playing!")
            sys.exit()

        print(f"Money: {money}")
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print(f"Bet: {bet}")
        while True:  # For player actions.
            display_hands(player_hand, dealer_hand, False)
            print("\n")

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == "D":  # Double down
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet}")
                print(f"Bet: {bet}")

            if move in ("H", "D"):  # Hit/doubling down
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:  # Player has busted
                    continue

            if move in ("S", "D"):  # Stand/doubling down, player's turn is over.
                break

        # For dealer actions.
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break  # The dealer has busted.
                input("Press ENTER to continue...")
                print("\n\n")

        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)
        # Find whether the player won, lost or game is a tie.
        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print("You lost!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You won ${bet}.")
        elif player_value == dealer_value:
            print("It's a tie. You got your money back.")

        input("Press ENTER to continue...")
        print("\n\n")


if __name__ == "__main__":
    main()
