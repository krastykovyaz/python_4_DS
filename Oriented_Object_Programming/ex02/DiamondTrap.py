from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
#your code here
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        self.eyes = color
    
    def get_eyes(self):
        return self.eyes
    
    def set_hairs(self, tpe):
        self.hairs = tpe
    
    def get_hairs(self):
        return self.hairs