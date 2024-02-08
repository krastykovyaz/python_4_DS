from S1E9 import Character
from abc import ABC, abstractmethod

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.is_alive=is_alive
        self.family_name='Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
        

    def die(self):
        self.is_alive = False
        
    def __str__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return f"of Vector: ('Baratheon', 'brown', 'dark')>{{'first_name': '{self.first_name}', 'is_alive': {self.is_alive}, 'family_name': '{self.family_name}', 'eyes': '{self.eyes}', 'hairs': '{self.hairs}'}}"
    

    def __repr__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
# your code here
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes='blue'
        self.hairs='light'

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"of Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
   

    # decorator
    def create_lannister(first_name, is_alive=True):
    #your code here
        return Lannister(first_name, is_alive)