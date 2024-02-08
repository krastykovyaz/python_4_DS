class calculator:
    #your code here
    def __init__(self, val) -> None:
        self.val = val

    def __add__(self, object) -> None:
        self.val = [v+ object for v in self.val ]
        print(self.val)
    #your code here
    def __mul__(self, object) -> None:
        print([v* object for v in self.val ])
    #your code here
    def __sub__(self, object) -> None:
    #your code here
        print([v- object for v in self.val ])
    def __truediv__(self, object) -> None:
    #your code here
        if object != 0:
            print([v / object for v in self.val ])
        else:
            print('Devide by zero !')
        
