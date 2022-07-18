import random
import shutil
import sys
import time

PAUSE = 0.2
DENSITY = 0.1

# Global constants for the ducks.
DUCKLING_WIDTH = 5
LEFT = "left"
RIGHT = "right"
BEADY = "beady"
WIDE = "wide"
HAPPY = "happy"
ALOOF = "aloof"
CHUBBY = "chubby"
VERY_CHUBBY = "very chubby"
OPEN = "open"
CLOSED = "closed"
OUT = "out"
DOWN = "down"
UP = "up"
HEAD = "head"
BODY = "body"
FEET = "feet"

WIDTH = shutil.get_terminal_size()[0]


class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        self.part_to_display_next = HEAD

    def get_head_str(self):
        head_str = ""
        if self.direction == LEFT:

            if self.mouth == OPEN:
                head_str += ">"
            elif self.mouth == CLOSED:
                head_str += "="

            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += '" '
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += "^^"
            elif self.eyes == ALOOF:
                head_str += "``"

            head_str += ") "

        if self.direction == RIGHT:
            head_str += " ("

            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += ' "'
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += "^^"
            elif self.eyes == ALOOF:
                head_str += "``"

            if self.mouth == OPEN:
                head_str += "<"
            elif self.mouth == CLOSED:
                head_str += "="

        if self.body == CHUBBY:
            head_str += " "
        return head_str

    def get_body_str(self):
        body_str = "("
        if self.direction == LEFT:
            if self.body == CHUBBY:
                body_str += " "
            elif self.body == VERY_CHUBBY:
                body_str += "  "

            if self.wing == OUT:
                body_str += ">"
            elif self.wing == UP:
                body_str += "^"
            elif self.wing == DOWN:
                body_str += "v"

        if self.direction == RIGHT:
            if self.body == CHUBBY:
                body_str += " "
            elif self.body == VERY_CHUBBY:
                body_str += "  "

            if self.wing == OUT:
                body_str += "<"
            elif self.wing == UP:
                body_str += "^"
            elif self.wing == DOWN:
                body_str += "v"
        body_str += ")"

        if self.body == CHUBBY:
            body_str += " "
        return body_str

    def get_feet_str(self):
        if self.body == CHUBBY:
            return " ^^  "
        elif self.body == VERY_CHUBBY:
            return " ^ ^ "

    def get_next_body_part(self):
        if self.part_to_display_next == HEAD:
            self.part_to_display_next = BODY
            return self.get_head_str()
        elif self.part_to_display_next == BODY:
            self.part_to_display_next = FEET
            return self.get_body_str()
        elif self.part_to_display_next == FEET:
            self.part_to_display_next = None
            return self.get_feet_str()


def main():
    print("Press Ctrl-C to quit.")
    time.sleep(2)
    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duckling_object in enumerate(duckling_lanes):
            if duckling_object == None and random.random() <= DENSITY:
                duckling_object = Duckling()
                duckling_lanes[lane_num] = duckling_object

            if duckling_object != None:
                print(duckling_object.get_next_body_part(), end="")
                if duckling_object.part_to_display_next == None:
                    duckling_lanes[lane_num] = None
            else:
                print(" " * DUCKLING_WIDTH, end="")
        print("\n")
        sys.stdout.flush()
        time.sleep(PAUSE)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
