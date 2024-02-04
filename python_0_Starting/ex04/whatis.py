import sys

def check_odd_even(num):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    # Check if there is exactly one argument
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    # Try to convert the argument to an integer
    try:
        num = int(sys.argv[1])
        check_odd_even(num)
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
