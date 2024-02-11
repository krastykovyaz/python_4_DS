def slice_me(family, start, end):
    """
    Truncate a 2D array (list of lists) using slicing.

    Args:
        family (list): The 2D array to truncate.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        list: The truncated 2D array.

    Raises:
        TypeError: If the input is not a valid 2D array.

    This function prints the shape of the original array, truncates it using slicing,
    prints the shape of the truncated array, and returns the truncated array.
    """
    if not isinstance(family, list) or not all(isinstance(row, list) and len(row) == len(family[0]) for row in family):
        raise TypeError("The input must be a 2D array (list of lists)")

    print(f"My shape is : ({len(family)}, {len(family[0])})")

    # Truncate the array using slicing
    truncated_array = family[start:end + 1]

    print(f"My new shape is : ({len(truncated_array)}, {len(truncated_array[0])})")

    return truncated_array

def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
