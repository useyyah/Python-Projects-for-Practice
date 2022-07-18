import random

input("Press ENTER to begin...")

p1_name = input("Human player 1, enter your name: ")
p2_name = input("Human player 2, enter your name: ")
player_names = p1_name[:11].center(11) + "    " + p2_name[:11].center(11)

print("""HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/""")

print("\n")
print(player_names)
print("\n")
print(f"{p1_name}, you have a RED box in front of you.")
print(f"{p2_name}, you have a GOLD box in front of you.")
print("\n")
print(f"{p1_name}, you will get to look into your box.")
print(f"{p2_name.upper()}, close your eyes and don't look!")
input(f"When {p2_name} has closed their eyes, press ENTER.")
print("\n")
print(f"{p1_name}, here is the inside of your box:")

if random.randint(1, 2) == 1:
    carrot_in_first_box = True
else:
    carrot_in_first_box = False

if carrot_in_first_box:
    print("""
      ____VV____  
     |    VV    |
     |    VV    |
     |____||____|    __________
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
     (Carrot!)""")
    print(player_names)
else:
    print("""
      __________  
     |          |
     |          |
     |__________|    __________
     /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
     (No Carrot!)""")
    print(player_names)

input("Press ENTER to continue.")

print("\n" * 100)  # For clearing the screen.
print(f"{p1_name}, tell {p2_name} to open their eyes.")
input("Press ENTER to continue.")

print("\n")
print(f"{p1_name}, have a conversation with {p2_name} whether you have the carrot or not.")
print("\n")
input("After that, press ENTER to continue.")
print("\n")

response = input(f"{p2_name}, do you want to swap boxes with {p1_name}? YES/NO").upper()
while True:
    if not (response.startswith("Y") or response.startswith("N")):
        print(f"{p2_name}, please enter 'YES' or 'NO'.")
    else:
        break

first_box = "RED"
second_box = "GOLD"

if response.startswith("Y"):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box

print("""HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/""".format(first_box, second_box))
print(player_names)
input("Press ENTER to reveal the winner!")
print("\n")

if carrot_in_first_box:
    print("""
      ____VV____     __________
     |    VV    |   |          |
     |    VV    |   |          |
     |____||____|   |__________|
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/""".format(first_box, second_box))

else:
    print("""    
       _________     ____VV____
      |         |   |    VV    | 
      |         |   |    VV    |
      |_________|   |____||____|
     /         /|   /    ||   /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/""".format(first_box, second_box))

print(player_names)
if carrot_in_first_box:
    print(f"{p1_name} is the winner!")
else:
    print(f"{p2_name} is the winner!")
print("Thanks for playing!")
