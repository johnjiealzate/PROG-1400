class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

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
    student_id = int(input("Enter student ID: "))
    new_grade = float(input("Enter new grade: "))
    sms.update_grade_by_id(student_id, new_grade)

    # Display all students after grade update
    print("\nAll Students after Grade Update:")
    sms.display_all_students()