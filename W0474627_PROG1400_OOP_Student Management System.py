# Define a class called `Student` with the following attributes.
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    # Implement appropriate methods within the `Student` class for the following tasks.
    def display_info(self, display_info):

# Define a subclass called `GraduateStudent`, inheriting from the `Student` class. Add an additional attribute.
class SraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic