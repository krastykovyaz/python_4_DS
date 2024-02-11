class Calculator:
    """
    A class for performing basic arithmetic operations on a list of values.
    """

    def __init__(self, values) -> None:
        """
        Initialize the Calculator with a list of values.

        Args:
            values (list): List of numeric values.
        """
        self.values = values

    def __add__(self, other) -> None:
        """
        Perform addition operation on the list of values.

        Args:
            other (float or int): Scalar value to add to each element in the list.
        """
        result = [v + other for v in self.values]
        print(result)

    def __mul__(self, other) -> None:
        """
        Perform multiplication operation on the list of values.

        Args:
            other (float or int): Scalar value to multiply with each element in the list.
        """
        result = [v * other for v in self.values]
        print(result)

    def __sub__(self, other) -> None:
        """
        Perform subtraction operation on the list of values.

        Args:
            other (float or int): Scalar value to subtract from each element in the list.
        """
        result = [v - other for v in self.values]
        print(result)

    def __truediv__(self, other) -> None:
        """
        Perform division operation on the list of values.

        Args:
            other (float or int): Scalar value to divide each element in the list by.
        """
        if other != 0:
            result = [v / other for v in self.values]
            print(result)
        else:
            print('Divide by zero!')

def main():
    """
    Main function to test the Calculator class.
    """
    values = [1, 2, 3, 4, 5]
    calc = Calculator(values)

    # Test addition
    calc + 5

    # Test multiplication
    calc * 10

    # Test subtraction
    calc - 3

    # Test division
    calc / 2

if __name__ == "__main__":
    main()
