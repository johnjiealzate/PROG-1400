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
    
# Step 2: Create an Object
# Creating an instance of the Rectangle class
# Create an instance my_rectangle of the Rectnagle class with a length of 5 and a width of 5
my_rectangle = Rectangle(length=5, width=5)

# Step 3: Access object attributes
print(f"Length: {my_rectangle.length}")
print(f"width: {my_rectangle.width}")

# Step 4: Call the methods of the object
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()
print("Area:", area)
print(f"Area of, my_rectangle, is {area}.")
print("Perimeter:", perimeter)