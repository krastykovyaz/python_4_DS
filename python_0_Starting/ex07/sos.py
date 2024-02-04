import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}

def encode_to_morse(text):
    """
    Encode the input text into Morse Code.

    Args:
    text (str): The input string to be encoded.

    Returns:
    str: The Morse Code representation of the input text.
    """
    return " ".join([NESTED_MORSE[char.upper()] for char in text if char.upper() in NESTED_MORSE])

def main():
    try:
        # Check the number of arguments
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")

        # Extract argument
        text = sys.argv[1]

        # Check argument type
        if not isinstance(text, str) or any([c for c in text if c.upper() not in NESTED_MORSE]):
            raise AssertionError("AssertionError: the arguments are bad")

        # Encode and print the result
        result = encode_to_morse(text)
        print(result)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
