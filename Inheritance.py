# Parent class
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def  speak(self):
        pass

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

'''
Objects are instances of the class.
Here, dogs and cats are instances of the Dog and Cat sub-classes
''' 
# Creating Objects
dog = Dog("Buddy", "domestic")
cat = Cat("Whisker", "domestic")

# Using methods
print(dog.speak())
print(cat.speak())