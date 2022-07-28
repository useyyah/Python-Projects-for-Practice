import math
import sys


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def main():
    while True:
        response = input("Enter a number to start searching for primes from:")
        if response.isdecimal():
            num = int(response)
            break

    input("Press Ctrl-C to quit any time.")

    while True:
        if is_prime(num):
            print(str(num) + ", ", end="", flush=True)
        num = num + 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
