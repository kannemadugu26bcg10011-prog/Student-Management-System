import json
import os

DATA_FILE = "students_data.json"


def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    print("\n--- Add Student Record ---")

    roll_number = input("Enter Roll Number: ")

    for student in students:
        if student["roll_number"] == roll_number:
            print("Student with this roll number already exists.")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = float(input("Enter Marks: "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "roll_number": roll_number,
        "name": name,
        "age": age,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("Student record added successfully.")


def view_students(students):
    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nRoll Number:", student["roll_number"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])


def search_student(students):
    print("\n--- Search Student ---")

    roll_number = input("Enter Roll Number: ")

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def class_performance(students):
    print("\n--- Class Performance Summary ---")

    if not students:
        print("No student records available.")
        return

    total_marks = sum(student["marks"] for student in students)
    average = total_marks / len(students)

    highest = max(students, key=lambda student: student["marks"])
    lowest = min(students, key=lambda student: student["marks"])

    passed = sum(1 for student in students if student["marks"] >= 50)
    failed = len(students) - passed

    print("Total Students:", len(students))
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest["marks"])
    print("Highest Scorer:", highest["name"])
    print("Lowest Marks:", lowest["marks"])
    print("Lowest Scorer:", lowest["name"])
    print("Passed Students:", passed)
    print("Failed Students:", failed)


def delete_student(students):
    print("\n--- Delete Student Record ---")

    roll_number = input("Enter Roll Number: ")

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            save_students(students)
            print("Student record deleted successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

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
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            class_performance(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
