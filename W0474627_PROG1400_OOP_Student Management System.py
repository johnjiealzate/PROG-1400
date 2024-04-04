class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Student Information: ID: {self.student_id} Name: {self.name} Age: {self.age} Grade: {self.grade}"

    def update_grade(self, new_grade):
        self.grade = new_grade


class GraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print()

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                return
        print("Student not found.")

    def update_grade_by_id(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(new_grade)
                print("Grade updated successfully.")
                return
        print("Student not found.")


# Demo
if __name__ == "__main__":
    # Create a StudentManagementSystem object
    sms = StudentManagementSystem()

    # Add some students
    student1 = Student(1, "Alice", 20, 85.5)
    student2 = GraduateStudent(2, "Bob", 25, 90.0, "Machine Learning")
    sms.add_student(student1)
    sms.add_student(student2)

    # Display all students
    print("All Students:")
    sms.display_all_students()
    print()

    # Search for a student by ID
    print("Search Student by ID:")
    sms.search_student_by_id(1)
    print()

    # Update grade of a student by ID
    print("Update Grade by ID:")
    sms.update_grade_by_id(2, 95.0)

    # Display all students after grade update
    print("\nAll Students after Grade Update:")
    sms.display_all_students()




'''# Define a class called `Student` with the following attributes.
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
          # self.students = []
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
StudentManagementSystem.see_all()'''
                    