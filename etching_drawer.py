import shutil
import sys

UP_DOWN_CHAR = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()

canvas = {}
cursor_X = 0
cursor_Y = 0


def get_canvas_string(canvas_data, cx, cy):
    canvas_str = ""
    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == cx and row_num == cy:
                canvas_str += "#"
                continue

            cell = canvas_data.get((column_num, row_num))
            if cell in (set(["W", "S"]), set(["W"]), set(["S"])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(["A", "D"]), set(["A"]), set(["D"])):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(["S", "D"]):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(["A", "S"]):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(["W", "D"]):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(["W", "A"]):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(["W", "S", "D"]):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(["W", "S", "A"]):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(["A", "S", "D"]):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(["W", "A", "D"]):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(["W", "A", "S", "D"]):
                canvas_str += CROSS_CHAR
            elif cell == None:
                canvas_str += " "
        canvas_str += "\n"
    return canvas_str


moves = []
while True:
    print(get_canvas_string(canvas, cursor_X, cursor_Y))
    response = input("WASD keys to move, H for help, C for clear, F to save, or QUIT.").upper()

    if response == "QUIT":
        print("Thanks for playing!")
        sys.exit()
    elif response == "H":
        print("Use WASD keys to draw lines.")
        print("\n")
        print("You can save your drawing to a txt file by entering F.")
        input("Press ENTER to return to the program...")
        continue
    elif response == "C":
        canvas = {}
        moves.append("C")
    elif response == "F":
        try:
            file_name = input("Enter the filename to save to:")
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write("".join(moves) + "\n")
                file.write(get_canvas_string(canvas, None, None))

        except:
            print("ERROR: Could not save the file.")

    for command in response:
        if command not in ("W", "A", "S", "D"):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ("W", "S"):
                canvas[(cursor_X, cursor_Y)] = set(["W", "S"])
            elif command in ("A", "D"):
                canvas[(cursor_X, cursor_Y)] = set(["A", "D"])

        if command == "W" and cursor_Y > 0:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_Y = cursor_Y - 1
        elif command == "S" and cursor_Y < CANVAS_HEIGHT - 1:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_Y = cursor_Y + 1
        elif command == "A" and cursor_X > 0:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_X = cursor_X - 1
        elif command == "D" and cursor_X < CANVAS_WIDTH - 1:
            canvas[(cursor_X, cursor_Y)].add(command)
            cursor_X = cursor_X + 1
        else:
            continue

        if (cursor_X, cursor_Y) not in canvas:
            canvas[(cursor_X, cursor_Y)] = set()

        if command == "W":
            canvas[(cursor_X, cursor_Y)].add("S")
        elif command == "S":
            canvas[(cursor_X, cursor_Y)].add("W")
        elif command == "A":
            canvas[(cursor_X, cursor_Y)].add("D")
        elif command == "D":
            canvas[(cursor_X, cursor_Y)].add("A")
