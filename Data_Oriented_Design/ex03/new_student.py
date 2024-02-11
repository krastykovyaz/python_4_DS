import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """Generate a random ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    """Class representing a student."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Set the login attribute after initialization."""
        self.login = self.name.capitalize() + self.surname.capitalize()
