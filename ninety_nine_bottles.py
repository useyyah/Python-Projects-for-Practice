import sys
import time

print("Press Ctrl-C to quit.")
time.sleep(2)

bottles = 99
PAUSE = 2

try:
    while bottles > 1:
        print(f"{bottles} bottles of milk on the wall,")
        time.sleep(PAUSE)
        print(f"{bottles} bottles of milk,")
        time.sleep(PAUSE)
        print("Take one down, pass it around,")
        time.sleep(PAUSE)
        bottles = bottles - 1
        print(f"{bottles} bottles of milk on the wall!")
        time.sleep(PAUSE)
        print("\n")

    print("1 bottle of milk on the wall,")
    time.sleep(PAUSE)
    print("1 bottle of milk,")
    time.sleep(PAUSE)
    print("Take it down pass it around,")
    time.sleep(PAUSE)
    print("No more bottles of milk on the wall!")
except KeyboardInterrupt:
    sys.exit()
