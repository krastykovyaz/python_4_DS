import sys
def filter_words_by_length(sentence, min_length):
    """
    Filter words from the sentence that have a length greater than min_length.

    Args:
    sentence (str): The input string containing words separated by spaces.
    min_length (int): The minimum length required for a word to be included in the output.

    Returns:
    list: A list of words from the sentence that have a length greater than min_length.
    """
    return list(filter(lambda word: len(word) > min_length, sentence.split()))

def main():
    """
    Main function to count characters in text.
    """
    try:
        # Check the number of arguments
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        # Extract arguments
        sentence = sys.argv[1]
        min_length = sys.argv[2]
        
        # Check argument types
        if not isinstance(sentence, str) or not min_length.isdigit():
            raise AssertionError("AssertionError: the arguments are bad")
        
        # Filter and print the result
        # result = filter_words_by_length(sentence, min_length)
        # print(result)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
