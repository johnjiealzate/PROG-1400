# Step 1: Create a rectangle class and define attributes and methods

# Create rectangle class (always start in )
class Rectangle:
    # Initialize the object attributes
    # self is the refrerence to the instance of the class. It is mandatory in every method.
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Define the method: calculate the area and perimeter to perform calculations based on attributes
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
# Create the child class
class Square(Rectangle):
    def __init__(self, side_length):
        # Call the constructor of the base class (Rectangle)
        super().__init__(length=side_length, width=side_length)
# Square is the new class that inderits from the Rectangle:
# The ___init___ method of the square calls the constructor
# of the base class (Rectangle) using
# super().___init___(length=side_length, width=side_length)
# This initializes the length and width attributes of the square
# using the same value.
# We don't need to define calculate_area and calculate_perimeter
# methods in the Square class, as it inherits them from the rectangle
    
# Step 2: Create an Object
# Creating an instance of the Rectangle class
my_rectangle = Rectangle(length=5, width=3)
# Create an instance my_square of the Rectangle class with a length of 5 and a width of 3
my_square = Square(side_length=5)


# Step 3: Access object attributes
print(f"Length: {my_rectangle.length}")
print(f"width: {my_rectangle.width}")
print(f"Side length: {my_square.width}")

# Step 4: Call the methods of the object
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()
print("Area:", area)
print("Perimeter:", perimeter)

# Calling inherited  methods
area_square = my_square.calculate_area()
perimeter_square = my_square.calculate_perimeter()
print("Area of the square:", area_square)
print("Perimeter of the square:", perimeter_square)


