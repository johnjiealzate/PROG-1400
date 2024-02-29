# Task 1: Abstraction
# Define a class named `Shape`.
from typing import Any


class Shape:
    def __init__(self):
        pass

    # Implement an abstract method `area()` within the `Shape` class.
    def calculate_area():
        return

 # Create two subclasses, `Rectangle` and `Circle`, inheriting from `Shape`.
class Rectangle(Shape):
    def __init__(self):
        super().__init__()

class Circle(Shape):
    def __init__(self):
        super().__init__()

# Task 3: Inheritance
# Define a base class named `Animal`.
class Animal:
    def __init__(self, name):
        self.name = name
 
    # Implement methods such as `speak()` and `move()` within the `Animal` class.
    def speak(self):
        pass

    def move(self):
        pass
 
# Create subclasses `Dog`, `Cat`, and `Bird`, inheriting from `Animal`.
# Override the `speak()` method for each subclass to reflect the respective animal's sound
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
 
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
 
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"
   
# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")
 
# Instantiate objects of each subclass and demonstrate their unique behaviors.
print(dog.speak())
print(cat.speak())
print(bird.speak())

print("\n")

# Task 4: Polymorphism
# Define a class named `Vehicle`.
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    # Implement a method `travel()` within the `Vehicle` class.
    def travel_method(self):
        pass

# Create subclasses `Car`, `Plane`, and `Bicycle`, inheriting from `Vehicle`.
class Car(Vehicle):
    def travel_method(self):
        # Override the `travel()` method for each subclass to reflect how they travel.
        return f"{self.name} travels by land."

class Plane(Vehicle):
    def travel_method(self):
        # Override the `travel()` method for each subclass to reflect how they travel.
        return f"{self.name} travels by air."
    
class Bicycle(Vehicle):
    def travel_method(self):
        # Override the `travel()` method for each subclass to reflect how they travel.
        return f"{self.name} travels by land."

 # Create objects
car = Car("Toyota Prius")
plane = Plane("Air Canada")
bicycle = Bicycle("Cannondale Bike")

    
# Instantiate objects of each subclass and demonstrate polymorphic behavior by calling the `travel()` method.
def travel(vehicle):
    return vehicle.travel_method()
 
vehicle = [car, plane, bicycle]
 
for vehicle in vehicle:
    print(travel(vehicle))
print("\n")    
