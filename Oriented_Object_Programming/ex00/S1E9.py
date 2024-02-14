from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the character with a first name and health state."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to change the health state of the character."""
        pass


class Stark(Character):
    """Subclass representing a Stark character."""

    def die(self):
        """Change the health state of the Stark character to dead."""
        self.is_alive = False
