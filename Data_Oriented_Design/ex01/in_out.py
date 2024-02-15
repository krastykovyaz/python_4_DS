def square(x: int | float) -> int | float:
    """
    Returns the square of a number.

    Args:
        x (int | float): The number to be squared.

    Returns:
        int | float: The square of the input number.
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """
    Raises a number to the power of itself.

    Args:
        x (int | float): The base number.

    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that applies the given function repeatedly on the input.

    Args:
        x (int | float): The initial value.
        function (function): The function to be applied.

    Returns:
        function: A function that applies
        the given function repeatedly on the input.
    """
    try:
        count = 0
        last_x = x

        def inner() -> float:
            """
            Applies the given function on the last result.

            Returns:
                float: The result of applying the function on the last result.
            """
            nonlocal count
            nonlocal last_x
            res = function(last_x)
            last_x = res
            count += 1
            return res

        return inner
    except Exception as e:
        print(e)
