import copy
import sys

TOTAL_DISKS = 5
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def ask_for_player_move(towers):
    while True:
        print("Enter the letters of 'from' and 'to' towers, or QUIT.")
        print("(e.g. AB to moves a disk from tower A to tower B.)")
        response = input(" ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA, or CB.")
            continue

        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            print("You selected a tower with no disks.")
            continue
        elif len(towers[to_tower]) == 0:
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue
        else:
            return from_tower, to_tower


def display_towers(towers):
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])
        print("\n")
    empty_space = " " * TOTAL_DISKS
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))


def display_disk(width):
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        print(empty_space + "||" + empty_space, end="")
    else:
        disk = "@" * width
        num_label = str(width).rjust(2, "_")
        print(empty_space + disk + num_label + disk + empty_space, end="")


def main():
    print("The Tower of Hanoi")
    print("""
    Move the tower of disks, one disk at a time, to another tower. Larger
    disks cannot rest on top of a smaller disk.
    """)

    towers = {"A": copy.copy(COMPLETE_TOWER), "B": [], "C": []}

    while True:
        display_towers(towers)

        from_tower, to_tower = ask_for_player_move(towers)

        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        if COMPLETE_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)
            print("You have solved the puzzle. Well done!")
            sys.exit()


if __name__ == "__main__":
    main()
