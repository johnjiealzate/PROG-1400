class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
   
    def get_stops(self, route):
        for stops in range(len(route)):
            if stops[0] or stops[len(route) - 1] == False:
                return stops
           
    def make_trip(self, route):
        print(f"{self.first_name} {self.last_name} is making a trip along the route: {route} ")  
 
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_color, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.car_make = v_make
        self.car_model = v_model
        self.v_type = v_type
        self.v_color = v_color
       
    def make_trip(self, route):
        print(f"{self.first_name} {self.last_name} is driving a {self.v_color} {self.v_type} along the {route} leaving {route[0]}, arriving at {route[len(route) -1]} and stopping at {route}")
       
class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)
       
    def make_trip(self, route):
        print(f"{self.first_name} {self.last_name} will pick you up along the {route} route")
       
class Route:
    def __init__(self, stops):
        self.stops = stops
       
driver1 = Driver("Davis", "Tom", "90299999", "db@db", "Honda", "Element", "Silver", "SUV")
rider1 = Rider("John", "Doe", "902-22222-222", "db@db.com")
route = ["Antigonish", "Tim Hortons", "Strait Area"]
 
 
 
# Polymorphism - Different types of persons can make trips using the same method name
driver1.make_trip(route)
rider1.make_trip(route)