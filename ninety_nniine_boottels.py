import random
import sys
import time

SPEED = 0.01
LINE_PAUSE = 1.5


def slow_print(text, pause_amount=0.1):
    for character in text:
        print(character, flush=True, end="")
        time.sleep(pause_amount)
    print("\n")


print("Press Ctrl-C to quit.")
time.sleep(2)
bottles = 99

lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:
        slow_print(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slow_print(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slow_print(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1

        if bottles > 0:
            slow_print(str(bottles) + lines[3], SPEED)
        else:
            slow_print("No more bottles of milk on the wall!", SPEED)

        time.sleep(LINE_PAUSE)
        print("\n")
        line_num = random.randint(0, 3)
        line = list(lines[line_num])

        effect = random.randint(0, 3)
        if effect == 0:  # Replace the character with a space.
            char_index = random.randint(0, len(line) - 1)
            line[char_index] = " "
        elif effect == 1:  # Change the casing of a character.
            char_index = random.randint(0, len(line) - 1)
            if line[char_index].isupper():
                line[char_index] = line[char_index].lower()
            elif line[char_index].islower():
                line[char_index] = line[char_index].upper()
        elif effect == 2:  # Transpose two characters.
            char_index = random.randint(0, len(line) - 2)
            first_char = line[char_index]
            second_char = line[char_index + 1]
            line[char_index] = second_char
            line[char_index + 1] = first_char
        elif effect == 3:  # Double a character.
            char_index = random.randint(0, len(line) - 2)
            line.insert(char_index, line[char_index])
        lines[line_num] = "".join(line)
except KeyboardInterrupt:
    sys.exit()
