# Step 1: Create a rectangle class and define attributes and methods
# Create rectangle class (always start in )
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def calculate_volume(self):
        pass

    def __str__(self):
        return self.__class__.__name__

# Create the child class Rectangle
class Rectangle(Shape):
    # Initialize the object attributes
    # self is the refrerence to the instance of the class. It is mandatory in every method.
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    # Define the method: calculate the area and perimeter to perform calculations based on attributes
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_volume(self):
        return self.length * self.width * self.height
    
# Create the child class Square
class Square(Rectangle):
    def __init__(self, side_length):
        # Call the constructor of the base class (Rectangle)
        super().__init__(length=side_length, width=side_length, height=side_length)

# Create the child class Circle
class Circle(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_area(self):
        return (3.14 *self.radius**2)
    
    def calculate_perimeter(self):
        return (2 * 3.14 * self.radius)

    def calculate_volume(self):
        return (3.14 *self.radius**2) * self.height

def print_area(shape):
    print(f"Area of the {shape} is {shape.calculate_area()}")

def print_perimeter(shape):
    print(f"Perimeter of the {shape} is {shape.calculate_perimeter()}")

def print_volume(shape):
    print(f"Volume of the {shape} is {shape.calculate_volume()}")

# Step 2: Create an Object
cuboid = Rectangle(length=5, width=3, height=5)
cube = Square(side_length=5)
cylinder = Circle(radius=5, height=5)

# Step 3: Access object attributes


# Step 4: Call the methods of the object
print_area(cuboid)
print_perimeter(cuboid)
print_volume(cuboid)