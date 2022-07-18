import random
import time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 21
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6
REWARD = 4
PENALTY = 1

assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)
ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print(f"""Add up all the dices displayed on the screen. You have
{QUIZ_DURATION} seconds to answer as many as you can. You get {REWARD} points for correct answers,
and lose {PENALTY} point for incorrect answers.""")
input("Press ENTER to begin...")

correct_answers = 0
incorrect_answers = 0
start_time = time.time()
while time.time() < start_time + QUIZ_DURATION:
    sum_answer = 0
    dice_faces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        dice_faces.append(die[0])
        sum_answer += die[1]

    top_left_dice_corners = []
    for i in range(len(dice_faces)):
        while True:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
            top_left_X = left
            top_left_Y = top
            top_right_X = left + DICE_WIDTH
            top_right_Y = top
            bottom_left_X = left
            bottom_left_Y = top + DICE_HEIGHT
            bottom_right_X = left + DICE_WIDTH
            bottom_right_Y = top + DICE_HEIGHT

            overlaps = False
            for prev_die_left, prev_die_top in top_left_dice_corners:
                prev_die_right = prev_die_left + DICE_WIDTH
                prev_die_bottom = prev_die_top + DICE_HEIGHT
                for corner_X, corner_Y in ((top_left_X, top_left_Y),
                                           (top_right_X, top_right_Y),
                                           (bottom_left_X, bottom_left_Y),
                                           (bottom_right_X, bottom_right_Y)):
                    if prev_die_left <= corner_X < prev_die_right and prev_die_top <= corner_Y < prev_die_bottom:
                        overlaps = True
            if not overlaps:
                top_left_dice_corners.append((left, top))
                break

    # Draw the dice on the canvas.
    canvas = {}
    for i, (die_left, die_top) in enumerate(top_left_dice_corners):
        die_face = dice_faces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvas_X = die_left + dx
                canvas_Y = die_top + dy
                canvas[(canvas_X, canvas_Y)] = die_face[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), " "), end="")
        print("\n")

    response = input("Enter the sum: ").strip()
    if response.isdecimal() and int(response) == sum_answer:
        correct_answers += 1
    else:
        print(f"Incorrect, the answer is {sum_answer}")
        time.sleep(2)
        incorrect_answers += 1

score = (correct_answers * REWARD) + (incorrect_answers * PENALTY)
print(f"Correct: {correct_answers}")
print(f"Incorrect: {incorrect_answers}")
print(f"Score: {score}")
print("Thanks for playing!")
