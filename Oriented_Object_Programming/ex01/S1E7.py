from abc import ABC, abstractmethod
from S1E9 import Character

class Baratheon(Character):
    """
    Representing the Baratheon family.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Baratheon character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Change the living status of the character to False."""
        self.is_alive = False
        
    def __str__(self) -> str:
        """
        Return a string representation of the Baratheon character.

        Returns:
            str: String representation of the character.
        """
        return f"{{'first_name': '{self.first_name}', 'is_alive': {self.is_alive}, 'family_name': '{self.family_name}', 'eyes': '{self.eyes}', 'hairs': '{self.hairs}'}}"
    
    def __repr__(self) -> str:
        """
        Return a string representation of the Baratheon character.

        Returns:
            str: String representation of the character.
        """
        return f"{{'first_name': '{self.first_name}', 'is_alive': {self.is_alive}, 'family_name': '{self.family_name}', 'eyes': '{self.eyes}', 'hairs': '{self.hairs}'}}"

class Lannister(Character):
    """
    Representing the Lannister family.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Change the living status of the character to False."""
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of the Lannister character.

        Returns:
            str: String representation of the character.
        """
        return f"{{'first_name': '{self.first_name}', 'is_alive': {self.is_alive}, 'family_name': '{self.family_name}', 'eyes': '{self.eyes}', 'hairs': '{self.hairs}'}}"

    def __repr__(self):
        """
        Return a string representation of the Lannister character.

        Returns:
            str: String representation of the character.
        """
        return f"{{'first_name': '{self.first_name}', 'is_alive': {self.is_alive}, 'family_name': '{self.family_name}', 'eyes': '{self.eyes}', 'hairs': '{self.hairs}'}}"

    def create_lannister(first_name, is_alive=True):
        """
        Create a Lannister character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The living status of the character. Defaults to True.

        Returns:
            Lannister: A Lannister character object.
        """
        return Lannister(first_name, is_alive)
