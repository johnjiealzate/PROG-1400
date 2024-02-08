class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name =  last_name
        self.mobile = mobile
        self.email = email

    def make_trip(self, route):
        print(f"{self.first_name, self.last_name} is making a trip along route {route}.")
                    
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)

class Driver(Person):
	def __init__(self, first_name, last_name, mobile, email, v_maker, v_model, v_type, v_color):
		super().__init__(first_name, last_name, mobile, email)
		self.v_maker = v_maker
		self.v_model = v_model
		self.v_type = v_type
		self.v_color = v_color

	def make_trip(self, route):
		print("f{self.first_name, self,last_name} is driving a {self._color, self.v_make, self.v_model, self.v_type}")

class Rider(Person):
	def __init__(self, first_name, last_name, mobile, email):
		super().__init__(first_name, last_name, mobile, email)
	
	def make_trip(self, route):
		print("f{self.first_name, self.last_name} will pick you up along {route}.")
driver1 = Driver("Johnjie", "Alzate", "902-555-1234", "ja@ja.com", "Honda", "Element", "Silver", "SUV")
rider1 = Rider("John", "Doe", "782-555-4444", "jd@jd.com")

route = ["Antigonish", "Tim Hortons", "Starit Area"]

driver1.make_trip(route)
rider1.make_trip(route)