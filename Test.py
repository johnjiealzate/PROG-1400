# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def  speak(self):
        pass

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class CAt(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
# Creating Objects
dog = Dog("Buddy")
cat = Cat("")