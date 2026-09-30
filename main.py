import csv
import os

FILE_NAME = "students.csv"
students = []


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_marks(subject):
    while True:
        try:
            marks = float(input("Enter marks in " + subject + ": "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def save_to_csv():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = [
            "id", "name", "physics", "chemistry", "maths",
            "total", "average", "grade"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def load_from_csv():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "id": row["id"],
                "name": row["name"],
                "physics": float(row["physics"]),
                "chemistry": float(row["chemistry"]),
                "maths": float(row["maths"]),
                "total": float(row["total"]),
                "average": float(row["average"]),
                "grade": row["grade"]
            }

            students.append(student)


def add_student():
    student_id = input("Enter student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"].lower() == student_id.lower():
            print("Student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    physics = get_marks("Physics")
    chemistry = get_marks("Chemistry")
    maths = get_marks("Mathematics")

    total = physics + chemistry + maths
    average = total / 3
    grade = calculate_grade(average)

    student = {
        "id": student_id,
        "name": name,
        "physics": physics,
        "chemistry": chemistry,
        "maths": maths,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    save_to_csv()

    print("\nStudent added successfully.")
    print("Total:", round(total, 2))
    print("Average:", round(average, 2))
    print("Grade:", grade)


def view_students():
    if len(students) == 0:
        print("No students added yet.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        print("-------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Physics:", student["physics"])
        print("Chemistry:", student["chemistry"])
        print("Mathematics:", student["maths"])
        print("Total:", round(student["total"], 2))
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"].lower() == student_id.lower():
            print("\n========== STUDENT FOUND ==========")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Physics:", student["physics"])
            print("Chemistry:", student["chemistry"])
            print("Mathematics:", student["maths"])
            print("Total:", round(student["total"], 2))
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def analyze_student():
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"].lower() == student_id.lower():

            physics = student["physics"]
            chemistry = student["chemistry"]
            maths = student["maths"]

            if physics <= chemistry and physics <= maths:
                weak_subject = "Physics"
            elif chemistry <= physics and chemistry <= maths:
                weak_subject = "Chemistry"
            else:
                weak_subject = "Mathematics"

            print("\n========== PERFORMANCE ANALYSIS ==========")
            print("Name:", student["name"])
            print("Total:", round(student["total"], 2))
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print("Lowest Marks Subject:", weak_subject)
            return

    print("Student not found.")


def class_analysis():
    if len(students) == 0:
        print("No students available for analysis.")
        return

    total_average = sum(student["average"] for student in students)
    class_average = total_average / len(students)

    highest = max(students, key=lambda student: student["average"])
    lowest = min(students, key=lambda student: student["average"])

    physics_average = sum(student["physics"] for student in students) / len(students)
    chemistry_average = sum(student["chemistry"] for student in students) / len(students)
    maths_average = sum(student["maths"] for student in students) / len(students)

    print("\n========== CLASS ANALYSIS ==========")
    print("Number of Students:", len(students))
    print("Class Average:", round(class_average, 2))

    print("\nHighest Performer:")
    print(highest["name"], "-", round(highest["average"], 2))

    print("Lowest Performer:")
    print(lowest["name"], "-", round(lowest["average"], 2))

    print("\nSubject Averages:")
    print("Physics:", round(physics_average, 2))
    print("Chemistry:", round(chemistry_average, 2))
    print("Mathematics:", round(maths_average, 2))


def show_ranking():
    if len(students) == 0:
        print("No students available for ranking.")
        return

    ranked_students = sorted(
        students,
        key=lambda student: student["average"],
        reverse=True
    )

    print("\n========== STUDENT RANKING ==========")
    print("Rank  Name                 Average  Grade")
    print("---------------------------------------------")

    for rank, student in enumerate(ranked_students, start=1):
        print(
            f"{rank:<5} "
            f"{student['name']:<20} "
            f"{student['average']:<8.2f} "
            f"{student['grade']}"
        )


def main():
    load_from_csv()

    while True:
        print("\n===================================")
        print("   STUDENT PERFORMANCE SYSTEM")
        print("===================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Analyze Student")
        print("5. Class Analysis")
        print("6. Student Ranking")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            analyze_student()

        elif choice == "5":
            class_analysis()

        elif choice == "6":
            show_ranking()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
