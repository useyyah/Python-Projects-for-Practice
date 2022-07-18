import datetime
import random


def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        first_birthday_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = first_birthday_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def match_birthdays(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a


MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:
    response = input("How many birthdays shall I generate? (Max 100)")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break

print("\n")

# Generating and displaying the birthdays
print(f"There are {num_bdays} birthdays:")
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(",", end="")
    month_name = MONTHS[birthday.month - 1]
    print(f"{month_name} {birthday.day}", end="")
print("\n\n")

match = match_birthdays(birthdays)

# Displaying the results
print("In this simulation ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    print(f"multiple people have a birthday on {month_name} {match.day}.")
else:
    print("There are no matching birthdays.")
print("\n")

print(f"Generating {num_bdays} random birthdays 100,000 times...")
input("Press ENTER to begin.")

print("Let's run another 100,000 simulations.")
sim_match = 0  # To show how many simulations have matching birthdays.
for i in range(100000):
    if i % 10000 == 0:  # To report progress for every 10,000 simulations
        print(f"{i} simulations run.")
    birthdays = get_birthdays(num_bdays)
    if match_birthdays(birthdays) is not None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# For displaying simulation results:
prob = round(sim_match / (100000 * 10), 2)
print(f"""Out of 100,000 simulations of {num_bdays} people, there was a
      matching birthday {sim_match} times. This means
      that {num_bdays} people have a {prob}% probability of having a matching
      birthday in their group.""")
