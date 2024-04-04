# Define a class called `Student` with the following attributes.
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    # Implement appropriate methods within the `Student` class for the following tasks.
    def display_info(self):
        return f"Student Information: ID: {self.student_id} Name: {self.name} Age: {self.age} Grade: {self.grade}"
    
    def update_info(self):
        self.name = input("Enter new name: ")
        self.age = input("Enter new age: ")
        self.grade = input("Enter new age: ")

# Define a subclass called `GraduateStudent`, inheriting from the `Student` class. Add an additional attribute.
class SraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic

    def display_info(self):
        return f"Name: {self.name} Thesis: {self.thesis_topic}"

class StudentManagementSystem:
    # def __init__(self):
          #self.students = []
    def add_student():
        new_id = len(student_list) + 1
        new_name = input()
        new_age = input()
        new_grade = input()
        student_list.append(Student(new_id, new_name, new_age, new_grade))
     
    def search_student_by_id(self, student_id):
        print ("Search student:")
        for student in self.students:
            if student.student_id == student_id:
                print ("Student found")
                student.display_info()
                return
            print("Student not found")

    def see_all():
        for i in student_list:
            print(i)

student_list = []

student_list.append(Student(1, "John", 20, 90))
student_list.append(Student(2, "Jane", 25, 85))

print(student_list)
StudentManagementSystem.see_all()
                    