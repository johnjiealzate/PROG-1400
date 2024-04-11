# Define a class called `Student` with the following attributes
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student information (`display_info()`).
    def display_info(self):
        print(f"Student ID: {self.student_id} Name: {self.name} Age: {self.age} Grade: {self.grade}")

    # Method to update the student's grade (`update_grade()`). 
    def update_grade(self, new_grade):
        self.grade = new_grade

# Define a subclass called `GraduateStudent`, inheriting from the `Student` class. Add an additional attribute
class GraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic

    # Display the thesis topic of the graduate student
    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")

# Create a class named `StudentManagementSystem` which will manage a list of students
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Implement a method to add a new student (`add_student()`).
    def add_student(self, student):
        self.students.append(student)

    # Implement a method to display information of all students (`display_all_students()`). 
    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print()

    # Implement a method to search for a student by ID and display their information (`search_student_by_id()`).
    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                return
        print("Student not found.")

    # Implement a method to update the grade of a student by ID (`update_grade_by_id()`). 
    def update_grade_by_id(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.update_grade(new_grade)
                print("Grade updated successfully.")
                return
        print("Student not found.")

    # Implement a method to add new students
    def add_new_student(self, student_id, name, age, grade, thesis_topic=None):
        if thesis_topic:
            new_student = GraduateStudent(student_id, name, age, grade, thesis_topic)
        else:
            new_student = Student(student_id, name, age, grade)
        self.add_student(new_student)
        print("New student added successfully.")

# Main script
if __name__ == "__main__":
    # Create a StudentManagementSystem object
    student_mgmt_sys = StudentManagementSystem()

    # Add students
    student1 = Student(1, "John", 21, 95.5)
    student2 = GraduateStudent(2, "Jane", 24, 88.6, "Augmented Reality")
    student3 = GraduateStudent(3, "Johnjie", 22, 94.5, "Artificial Intelligence")
    student4 = Student(4, "Cameron", 21, 89)
    student_mgmt_sys.add_student(student1)
    student_mgmt_sys.add_student(student2)
    student_mgmt_sys.add_student(student3)
    student_mgmt_sys.add_student(student4)

    # Display information of all students
    print("All Students:")
    student_mgmt_sys.display_all_students()
    print()

    # Search for a student by ID
    print("Search Student by ID:")
    student_mgmt_sys.search_student_by_id(1)
    print()

    # Update grade of a student by ID
    print("Update Grade by ID:")
    student_id = int(input("Enter student ID: "))
    new_grade = float(input("Enter new grade: "))
    student_mgmt_sys.update_grade_by_id(student_id, new_grade)

    # Display all students after grade update
    print("\nAll Students after Grade Update:")
    student_mgmt_sys.display_all_students()
    print()

    # Add new student
    print("Add New Student:")
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    is_graduate = input("Is the student a graduate student? (yes/no): ").lower()
    if is_graduate == "yes":
        thesis_topic = input("Enter thesis topic: ")
        student_mgmt_sys.add_new_student(student_id, name, age, grade, thesis_topic)
    else:
        student_mgmt_sys.add_new_student(student_id, name, age, grade)

    # Display all students after adding new student
    print("\nAll Students after Adding New Student:")
    student_mgmt_sys.display_all_students()