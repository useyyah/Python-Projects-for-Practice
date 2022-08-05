import copy
import random
import sys

EMPTY_SPACE = "."
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, original_setup):
        self.original_setup = original_setup
        self.grid = {}
        self.reset_grid()  # Set the grid to its original setup.
        self.moves = []  # Tracks each move.

    def reset_grid(self):
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.original_setup) == FULL_GRID_SIZE
        i = 0
        y = 0
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.original_setup[i]
                i += 1
            y += 1

    def make_move(self, column, row, number):
        x = "ABCDEFGHI".find(column)
        y = int(row) - 1

        if self.original_setup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False
        self.grid[(x, y)] = number

        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        if self.moves == []:
            return

        self.moves.pop()

        if self.moves == []:
            self.reset_grid()
        else:
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        print('   A B C   D E F   G H I')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    print(str(y + 1) + "  ", end="")

                print(self.grid[(x, y)] + " ", end="")
                if x == 2 or x == 5:
                    print("| ", end="")
            print("\n")

            if y == 2 or y == 5:
                print('   ------+-------+------')

    def is_complete_set_of_numbers(self, numbers):
        return sorted(numbers) == list("123456789")

    def is_solved(self):
        # Check rows.
        for row in range(GRID_LENGTH):
            row_numbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                row_numbers.append(number)
            if not self.is_complete_set_of_numbers(row_numbers):
                return False

        # Check columns.
        for column in range(GRID_LENGTH):
            column_numbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                column_numbers.append(number)
            if not self.is_complete_set_of_numbers(column_numbers):
                return False

        # Check boxes.
        for box_x in (0, 3, 6):
            for box_y in (0, 3, 6):
                box_numbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(box_x + x, box_y + y)]
                        box_numbers.append(number)
                if not self.is_complete_set_of_numbers(box_numbers):
                    return False
        return True


print("Sudoku Puzzle")
input("Press ENTER to begin.")

with open("sudokupuzzle.txt") as puzzle_file:
    puzzles = puzzle_file.readlines()

for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))

while True:  # Main game loop.
    grid.display()

    # Check if the puzzle is solved.
    if grid.is_solved():
        print("Congratulations! You solved the puzzle.")
        print("Thanks for playing.")
        sys.exit()

    # Get the player's action.
    while True:
        print("\n")
        action = input("Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT: ").upper().strip()

        if len(action) > 0 and action[0] in ("R", "N", "U", "O", "Q"):
            break

        if len(action.split()) == 2:
            space, number = action.split()
            if len(space) != 2:
                continue

            column, row = space
            if column not in list("ABCDEFGHI"):
                print(f"There is no column {column}")
                continue
            if not row.isdecimal() or not (1 <= int(row) <= 9):
                print(f"There is no row {row}")
                continue
            if not (1 <= int(number) <= 9):
                print("Please select a number from 1 to 9.")
                continue
            break

    print("\n")

    if action.startswith("R"):
        grid.reset_grid()
        continue

    if action.startswith("N"):
        grid = SudokuGrid(random.choice(puzzles))
        continue

    if action.startswith("U"):
        grid.undo()
        continue

    if action.startswith("O"):
        original_grid = SudokuGrid(grid.original_setup)
        print("The original grid looked like this:")
        original_grid.display()
        input("Press ENTER to continue.")

    if action.startswith("Q"):
        print("Thanks for playing.")
        sys.exit()

    # Handle the move the player selected.
    if grid.make_move(column, row, number) == False:
        print("You cannot overwrite the original grid's numbers.")
        input("Press ENTER to contniue.")
