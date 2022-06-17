class DivisionByZeroError(Exception):
    pass

class Calculator:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            raise DivisionByZeroError
        return self.x / self.y