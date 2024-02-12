def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> ft_filter object

    Return an iterator yielding those items of iterable\
    for which function(item)
    is true. If function is None, return the items that are true.
    """
    elems = []
    for element in iterable:
        is_true = function(element)
        if is_true is True:
            elems.append(element)
        elif is_true is None:
            elems.append(element)
    return elems


def main():
    # Test your ft_filter function
    # Example 1
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(x):
        return x % 2 == 0

    filtered_numbers = ft_filter(is_even, numbers)
    print(filtered_numbers)

    # Example 2
    words = ["apple", "banana", "cherry", "date", "elderberry"]

    def has_letter_a(word):
        return 'a' in word

    filtered_words = ft_filter(has_letter_a, words)
    print(filtered_words)


if __name__ == "__main__":
    main()
    print(filter.__doc__)
