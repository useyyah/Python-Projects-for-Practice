def display_outline_diamond(size):
    # Top half
    for i in range(size):
        print(" " * (size - i - 1), end="")  # Left side space.
        print("/", end="")  # Left side of diamond.
        print(" " * (i * 2), end="")  # Interior of diamond.
        print("\\")  # Right side of diamond.

    # Bottom half
    for i in range(size):
        print(" " * i, end="")  # Left size space.
        print("\\", end="")  # Left side of diamond.
        print(" " * ((size - i - 1) * 2), end="")  # Interior of diamond.
        print("/")  # Right side of diamond.


def display_filled_diamond(size):
    # Top half.
    for i in range(size):
        print(" " * (size - i - 1), end="")  # Left side space.
        print("/" * (i + 1), end="")  # Left half of diamond.
        print("\\" * (i + 1))  # Right half of diamond.

    for i in range(size):
        print(" " * i, end="")  # Left size space.
        print("\\" * (size - i), end="")  # Left side of diamond.
        print("/" * (size - i))  # Right side of diamond.


def main():
    for diamond_size in range(0, 6):
        display_outline_diamond(diamond_size)
        print("\n")
        display_filled_diamond(diamond_size)
        print("\n")


if __name__ == "__main__":
    main()
