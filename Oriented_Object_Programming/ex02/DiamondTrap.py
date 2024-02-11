from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """
    Class representing a king who inherits from Baratheon and Lannister families.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a King object.

        Args:
            first_name (str): The first name of the king.
            is_alive (bool): Indicates whether the king is alive. Default is True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Set the eye color of the king.

        Args:
            color (str): The eye color to set.
        """
        self.eyes = color
    
    def get_eyes(self):
        """
        Get the eye color of the king.

        Returns:
            str: The eye color of the king.
        """
        return self.eyes
    
    def set_hairs(self, tpe):
        """
        Set the hair type of the king.

        Args:
            tpe (str): The hair type to set.
        """
        self.hairs = tpe
    
    def get_hairs(self):
        """
        Get the hair type of the king.

        Returns:
            str: The hair type of the king.
        """
        return self.hairs

def main():
    """
    Main function to test the King class.
    """
    # Test the King class methods
    king = King("Robert")
    print(king.__dict__)
    king.set_eyes("blue")
    king.set_hairs("blonde")
    print(king.get_eyes())
    print(king.get_hairs())

if __name__ == "__main__":
    main()
