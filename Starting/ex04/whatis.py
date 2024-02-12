import sys


def check_odd_even(num):
    """
    Checks if a number is odd or even and prints the result.

    Args:
        num (int): The number to check.

    Returns:
        None
    """
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    """
    Main function to check if a number is odd \
    or even based on command-line argument.
    """
    if len(sys.argv) < 2:
        sys.exit(0)
    # Check if there is exactly one argument
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    # Try to convert the argument to an integer
    try:
        num = int(sys.argv[1])
        check_odd_even(num)
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)


if __name__ == "__main__":
    main()
