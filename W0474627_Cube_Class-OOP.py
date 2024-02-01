# Step 1: Create a rectangle class and define attributes and methods

# Create rectangle class (always start in )
class Cube:
    # Initialize the object attributes
    # self is the refrerence to the instance of the class. It is mandatory in every method.
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def calculate_volume(self):
        return self.length * self.width * self.height
    
# Step 2: Create an Object
# Creating an instance of the Rectangle class
# Create an instance my_rectangle of the Rectnagle class with a length of 5, width of 5, and heigth of 5
my_cube = Cube(length=5, width=5, height=5)

# Step 3: Access object attributes
print(f"Length: {my_cube.length}")
print(f"width: {my_cube.width}")
print(f"width: {my_cube.height}")

# Step 4: Call the methods of the object
volume = my_cube.calculate_volume()
print("Volume:", volume)