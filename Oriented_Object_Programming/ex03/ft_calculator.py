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

    def __add__(self, object) -> None:
        """
        Perform addition operation on the list of values.

        Args:
            other (float or int):
            Scalar value to add to each element in the list.
        """
        try:
            result = [v + object for v in self.values]
            print(result)
        except Exception as e:
            print(e)

    def __mul__(self, object) -> None:
        """
        Perform multiplication operation on the list of values.

        Args:
            other (float or int):
            Scalar value to multiply with each element in the list.
        """
        try:
            result = [v * object for v in self.values]
            print(result)
        except Exception as e:
            print(e)

    def __sub__(self, object) -> None:
        """
        Perform subtraction operation on the list of values.

        Args:
            other (float or int):
            Scalar value to subtract from each element in the list.
        """
        try:
            result = [v - object for v in self.values]
            print(result)
        except Exception as e:
            print(e)

    def __truediv__(self, object) -> None:
        """
        Perform division operation on the list of values.

        Args:
            other (float or int):
            Scalar value to divide each element in the list by.
        """
        try:
            if object != 0:
                result = [v / object for v in self.values]
                print(result)
            else:
                print('Divide by zero!')
        except Exception as e:
            print(e)
