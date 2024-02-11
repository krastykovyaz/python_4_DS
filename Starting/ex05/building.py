import sys

def count_characters(text):
    """
    Count the number of upper-case characters, lower-case characters, punctuation characters,
    digits, and spaces in the given text.
    Args:
    text (str): The input text.
    Returns:
    dict: A dictionary containing the counts of each category.
    """
    char_count = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in text:
        if char.isupper():
            char_count['upper'] += 1
        elif char.islower():
            char_count['lower'] += 1
        elif char in '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~''':
            char_count['punctuation'] += 1
        elif char.isdigit():
            char_count['digits'] += 1
        elif char.isspace():
            char_count['spaces'] += 1

    return char_count

def main():
    """
    Main function to count characters in text.
    """
    if len(sys.argv) == 1:
        try:
            text = input("What is the text to count?\n")
        except EOFError:
            sys.exit(0)
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("More than one argument is provided")

    character_counts = count_characters(text)
    total_chars = sum(character_counts.values())

    print(f"The text contains {total_chars} characters:")
    for category, count in character_counts.items():
        if category == 'punctuation':
            print(f"{count} {category} marks")
        elif category == 'spaces':
            print(f"{count} {category}")
        elif category == 'digits':
            print(f"{count} {category}")
        else:
            print(f"{count} {category} letters")


if __name__ == "__main__":
    main()
