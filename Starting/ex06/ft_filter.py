def ft_filter(function, iterable):
    """
    Recoded version of the filter function using list comprehensions.
    
    Args:
    function (callable): The function used to test each element of the iterable.
    iterable (iterable): The iterable to filter.
    
    Returns:
    list: A list containing the elements from the iterable for which the function returns True.
    """
    return [element for element in iterable if function(element)]

def main():
    # Test your ft_filter function
    # Example 1
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_even = lambda x: x % 2 == 0
    filtered_numbers = ft_filter(is_even, numbers)
    print(filtered_numbers)

    # Example 2
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    has_letter_a = lambda word: 'a' in word
    filtered_words = ft_filter(has_letter_a, words)
    print(filtered_words)

if __name__ == "__main__":
    main()
    print(filter.__doc__)
