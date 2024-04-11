# Task 1: Abstraction
# Define a class named `Shape`.
class Shape:
    # Implement an abstract method `area()` within the `Shape` class.
    def calculate_area(self):
        return 
    
    def __str__(self):
        return self.__class__.__name__

# Create two subclasses, `Rectangle` and `Circle`, inheriting from `Shape`.
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Implement the `area()` method for `Rectangle` classes.
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Implement the `area()` method for `Circle` classes.
    def calculate_area(self):
        return 3.14 * self.radius**2
    
# Instantiate objects of both `Rectangle` and `Circle` classes and demonstrate the calculation of their areas.
def print_area(shape):
    print(f"Area of the {shape} is {shape.calculate_area()}")

rectangle = Rectangle(length=10, width=10)
circle = Circle(radius=5)

print_area(rectangle)
print_area(circle)
print("\n")    

# Task 2: Abstraction
# Define a class called `Student` with the following attributes.
class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__grade = ""

    # Implement methods to set and get these details.
    def display_info(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def input_name(self):
        return self.__name
    
    def input_age(self):
        return self.__age
    
    def input_grade(self):
        return self.__grade
    
# Demonstrate the use of these methods by creating instances of the `Student` class and manipulating their details.
student1 = Student()
name = input("What is your name?")
age = input("What is your age?")
grade = input("What is your grade?")

student1.display_info(name, age, grade)
print("Student Name:", student1.input_name())
print("Student Age:", student1.input_age())
print("Student Grade:", student1.input_age())
print("\n")  

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
    
    def move(self):
        return f"{self.name} the dog walks."
 
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
    def move(self):
        return f"{self.name} the cat jumps."
 
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"
    
    def move(self):
        return f"{self.name} the bird flies."
   
# Instantiate objects of each subclass and demonstrate their unique behaviors.
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")
 
print(dog.speak())
print(cat.speak())
print(bird.speak())
print("\n")

print(dog.move())
print(cat.move())
print(bird.move())
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

# Instantiate objects of each subclass and demonstrate polymorphic behavior by calling the `travel()` method.
car = Car("Toyota Prius")
plane = Plane("Air Canada")
bicycle = Bicycle("Cannondale Bike")

def travel(vehicle):
    return vehicle.travel_method()
 
vehicle = [car, plane, bicycle]
 
for vehicle in vehicle:
    print(travel(vehicle))
print("\n")    
