# Polymorphism in Python allows objects of different types to

class Fruit:
    # Constructoe (___init___ method): 
    # Initialized the object with an owner and an optional initial balance
    def __init__(self, name):
        self.name = name

    # Method to return the string "Generic Taste"
    def taste (self):
        return "Generic Taste"

class Apple(Fruit):
    def __init__(self, name, color):
        # super() is a built-in function that is commonly used in the context
        # of object-oriented programming, specifically within classes that are
        # part of an inheritance hierarchy. It provides a way to access and 
        # call methods from a super class (parent class) ina subclass(child class).
        super().__init__(name)
        self.color = color

    def taste(self):
        generic_taste = super().taste() # Calling the supeclass method
        return f"{generic_taste} and Crispy"
    
def describe_taste(Fruit):
    print (f"{Fruit.name} taste: {Fruit.taste()}")

class Orange(Fruit):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
    def taste(self):
        generic_taste = super().taste() # Calling the supeclass method
        return f"{generic_taste} and Sour"

# Create instances of Apple and Orange
apple = Apple("Red Apple", "Red")
orange = Orange("Orange Orange", "Large")

# Demonstrate polymorphism by calling the describe_taste function with different fruit objects
describe_taste(apple)
describe_taste(orange)
