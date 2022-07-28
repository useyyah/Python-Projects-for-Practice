import math
import shutil
import sys
import time

WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1

print("Press Ctrl-C to quit.")
print("\n")
print(f"What message do you want to display? (Max {WIDTH // 2} chars.) ")
while True:
    message = input()
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print(f"Message must be 1 to {WIDTH // 2} characters long.")

step = 0
multiplier = (WIDTH - len(message)) / 2
try:
    while True:
        sin_of_step = math.sin(step)
        padding = " " * int((sin_of_step + 1) * multiplier)
        time.sleep(0.1)
        step += 0.25
except KeyboardInterrupt:
    sys.exit()
