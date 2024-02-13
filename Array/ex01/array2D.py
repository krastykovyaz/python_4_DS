import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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

    This function prints the shape of the original array,
    truncates it using slicing,
    prints the shape of the truncated array, and returns the truncated array.
    """
    try:
        if not isinstance(family, list) or \
                not isinstance(start, int) \
                or not isinstance(end, int):
            raise AssertionError("Input must be a list or integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except Exception as e:
        print(e)
