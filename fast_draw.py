import random
import sys
import time

print("When you see 'DRAW', you have 0.3 seconds to press ENTER.")
print("But you will lose if you press ENTER before 'DRAW' appears.")
print("\n")
input("Press ENTER to begin.")

while True:
    print("\n")
    print("Get ready!!!")
    time.sleep(random.randint(20, 50) / 10)
    print("DRAW")
    draw_time = time.time()
    input()
    time_elapsed = time.time() - draw_time

    if time_elapsed < 0.01:
        print("You drew before 'DRAW' appeared. You lose!")
    elif time_elapsed > 0.3:
        time_elapsed = round(time_elapsed, 4)
        print(f"You draw in {time_elapsed} seconds. Too slow!")
    else:
        time_elapsed = round(time_elapsed, 4)
        print(f"You draw in {time_elapsed} seconds. You WON!")

    response = input("Input QUIT to stop, or press ENTER to play again.").upper()
    if response == "QUIT":
        print("Thanks for playing!")
        sys.exit()
