class AdvancedCalculator:
    @staticmethod
    def exponentiate(base, exponent):
        return base ** exponent
    
# Define functions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y  == 0:
        raise ValueError("Cannot divide by zero")
    return x / y