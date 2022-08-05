import playsound
import random
import time

input("Press ENTER to begin.")

pattern = ""
while True:
    print("\n" * 60)

    pattern = pattern + random.choice("ASDF")

    print("Pattern: ", end="")
    for letter in pattern:
        print(letter, end="", flush=True)
        playsound.playsound("sound" + letter + ".wav")

    time.sleep(1)
    print("\n" * 60)

    response = input("Enter the patter: ").upper()

    if response != pattern:
        print("Incorrect!")
        print(f"The pattern was {pattern}")
    else:
        print("Correct!")

    for letter in pattern:
        playsound.playsound("sound" + letter + ".wav")

    if response != pattern:
        print(f"You scored {len(pattern) - 1} points.")
        print("Thanks for playing!")
        break

    time.sleep(1)
