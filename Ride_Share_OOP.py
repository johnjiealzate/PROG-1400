from datetime import datetime
# Encapsulation: Attributes and methods are encapsulated within the class
class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
    
    def details(self):
        return f"Name: {self.first_name} {self.last_name}, Mobile: {self.mobile}, Email: {self.email}"
  
# Inheritance: Driver and Rider inherits from the class Person  

class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_color, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_type = v_type
        self.v_color = v_color
        
    def details(self):
        return f"Driver {super().details()}, Vehicle: {self.v_color} {self.v_make} {self.v_model} {self.v_type}"
    
class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)
    
    def details(self):
        return f"Rider {super().details()}"

# Abstraction: Users interact with the classes through their interfcaes (details() method),    
# hiding the complexities of their implementations.

class Route:
    def __init__(self, origin, midway_stop, destination) -> None:
        self.origin = origin
        self.midway_stop = midway_stop
        self.destination = destination
        
    def details(self):
        return f"Trip Origin: {self.origin}, Midway Stop: {self.midway_stop}, Destination: {self.destination}"

# Polymorphism: The details() method is polymorphic - it behaves differently based on the object calling it.    

class Trip(Route):
    def __init__(self, origin, midway_stop, destination, leaving_time, stop_time, arrival_time) -> None:
        super().__init__(origin, midway_stop, destination)
        self.leaving_time = leaving_time
        self.stop_time = stop_time
        self.arrival_time = arrival_time
        
    def details(self):
        return f"Trip Details: {super().details()}, Leaving Time: {self.leaving_time}, Stop Time: {self.stop_time}, Arrival Time: {self.arrival_time}"
    
def run():
    # Create instances of the classes.
    driver1 = Driver("Johnjie", "Alzate", "902-555-8888", "ja@ja.com", "Dodge", "Avenger", "Gray", "Car")
    rider1 = Rider("John", "Smith", "902-111-5555", "js@js.com")
    trip1 = Trip("Antigonish", "Tim Hortons", "Strait Area Campus", datetime(2024, 2, 15, 7, 0, 0), datetime(2024, 2, 15, 8, 0, 0), datetime(2024, 2, 15, 8, 30, 0))
    # Store instances in a list for iteration
    journey1 = [driver1, rider1, trip1]
    
    # Iterate over the entities and print the details
    for i in journey1:
        print("\n")
        print(i.details())
    
 # The __name__ variable is a specia variable that holds the name of the current
 # module. When a Python script is executed, Python sets the __name__ variable
 # for that script  to "__main__", in dicating that the script is being run directly,
 # not omported as a module.
 # The line if __name__ == "__name__": is a common idiom used in Python cripts.
 # It checks if the current script is being run directly by the Python interpreter.
 # If so, it executes the block of the code inside the if statement.
 # This is useful when you have a Pyhton file that can be both imported as a module
 # in other scripts andru as a standalone script.
 
if __name__ == "__main__":
    run()