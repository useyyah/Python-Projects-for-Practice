import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
COUNTRIES = ['Germany', 'Britain', 'India', 'Japan', 'Thai',
             'Algeria', 'Maori', 'Georgia', 'Ethiopia', 'Argentine']
NOUNS = ['Athlete', 'Clown', 'Scientist', 'Mathematician', 'Doctor', 'Parent',
         'Dentist', 'Historian', 'Statistician', 'Python Developer', 'Chemist', 'Seismologist',
         'Palaeontologist', 'Serial Killer', 'Geneticist']
PLACES = ['House', 'University', 'Bank Deposit Box', 'School', 'Basement', 'Hospital', 'Mine Shaft',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker', 'Bag', 'Subway Train', 'Mind']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week',
        'In About Half An Hour', 'At Some Point In The Near Future']


def main():
    while True:
        response = input("Enter the number of clickbait headlines to generate: ")
        if not response.isdecimal():
            print("Please enter a number.")
        else:
            number_of_headlines = int(response)
            break

    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            headline = generate_are_millennial_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automated_headline()
        print(headline)
    print("\n")


def generate_are_millennial_killing_headline():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing The {noun} industry"


def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return f"Without This {noun}, {plural_noun} Could Kill You {when}"


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(COUNTRIES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}"


def generate_you_wont_believe_headline():
    state = random.choice(COUNTRIES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generate_dont_want_you_to_know_headline():
    plural_noun1 = random.choice(NOUNS) + "s"
    plural_noun2 = random.choice(NOUNS) + "a"
    return f"What {plural_noun1} Don't Want You To Know About {plural_noun2}"


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(COUNTRIES)
    return f"{number} Gift Ideas to Give Your {noun} from {state}"


def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + "s"
    number2 = random.randint(1, number1)
    return f"{number1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"


def generate_job_automated_headline():
    state = random.choice(COUNTRIES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == "Their":
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong."


if __name__ == "__main__":
    main()
