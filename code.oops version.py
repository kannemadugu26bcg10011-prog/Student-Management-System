import json
import os


class Student:

    def __init__(self, roll_number, name, age, marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nRoll Number:", self.roll_number)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Grade:", self.grade)

    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "age": self.age,
            "marks": self.marks,
            "grade": self.grade
        }


class StudentManagementSystem:

    def __init__(self):
        self.data_file = "students_data.json"
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)

                for student in data:
                    self.students.append(
                        Student(
                            student["roll_number"],
                            student["name"],
                            student["age"],
                            student["marks"]
                        )
                    )

            except json.JSONDecodeError:
                self.students = []

    def save_students(self):
        data = []

        for student in self.students:
            data.append(student.to_dict())

        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self):
        print("\n--- Add Student Record ---")

        roll_number = input("Enter Roll Number: ")

        for student in self.students:
            if student.roll_number == roll_number:
                print("Student with this roll number already exists.")
                return

        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        marks = float(input("Enter Marks: "))

        student = Student(
            roll_number,
            name,
            age,
            marks
        )

        self.students.append(student)
        self.save_students()

        print("Student record added successfully.")

    def view_students(self):
        print("\n--- All Student Records ---")

        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        print("\n--- Search Student ---")

        roll_number = input("Enter Roll Number: ")

        for student in self.students:
            if student.roll_number == roll_number:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    def class_performance(self):
        print("\n--- Class Performance Summary ---")

        if not self.students:
            print("No student records available.")
            return

        total_marks = sum(
            student.marks for student in self.students
        )

        average = total_marks / len(self.students)

        highest = max(
            self.students,
            key=lambda student: student.marks
        )

        lowest = min(
            self.students,
            key=lambda student: student.marks
        )

        passed = sum(
            1 for student in self.students
            if student.marks >= 50
        )

        failed = len(self.students) - passed

        print("Total Students:", len(self.students))
        print("Average Marks:", round(average, 2))
        print("Highest Marks:", highest.marks)
        print("Highest Scorer:", highest.name)
        print("Lowest Marks:", lowest.marks)
        print("Lowest Scorer:", lowest.name)
        print("Passed Students:", passed)
        print("Failed Students:", failed)

    def delete_student(self):
        print("\n--- Delete Student Record ---")

        roll_number = input("Enter Roll Number: ")

        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                self.save_students()

                print("Student record deleted successfully.")
                return

        print("Student not found.")

    def run(self):

        while True:

            print("\n=============================================")
            print("       STUDENT RECORD & GRADE MANAGEMENT")
            print("=============================================")
            print("1. Add Student Record")
            print("2. View All Students")
            print("3. Search Student by Roll Number")
            print("4. View Class Performance Summary")
            print("5. Delete Student Record")
            print("6. Exit")
            print("=============================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.class_performance()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please try again.")


# Create object
system = StudentManagementSystem()

# Run the program
system.run()
