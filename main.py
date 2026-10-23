from student_service import add_student, view_students, search_student
from result_service import add_marks, view_results
from database import create_connection


def setup_subjects():
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        subjects = ["Python", "Java", "MySQL"]

        query = """
            INSERT IGNORE INTO subjects (subject_name)
            VALUES (%s)
        """

        for subject in subjects:
            cursor.execute(query, (subject,))

        connection.commit()
        print("Subjects setup completed successfully!")

    except Exception as error:
        if connection is not None:
            connection.rollback()
        print("Error setting up subjects:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def main():
    setup_subjects()

    while True:
        print("\n===== GradeSync =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Enter Marks")
        print("5. View Results")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                student_id = int(input("Enter student ID: "))
                student_name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()

                if not student_name:
                    print("Student name cannot be empty.")
                    continue

                add_student(
                    student_id,
                    student_name,
                    email if email else None
                )

            except ValueError:
                print("Student ID must be a number.")

        elif choice == "2":
            view_students()

        elif choice == "3":
            try:
                student_id = int(input("Enter student ID: "))
                search_student(student_id)

            except ValueError:
                print("Student ID must be a number.")

        elif choice == "4":
            try:
                student_id = int(input("Enter student ID: "))
                subject_id = int(
                    input(
                        "Enter subject ID "
                        "(1=Python, 2=Java, 3=MySQL): "
                    )
                )
                marks = float(input("Enter marks: "))

                if subject_id not in (1, 2, 3):
                    print("Invalid subject ID.")
                    continue

                if not 0 <= marks <= 100:
                    print("Marks must be between 0 and 100.")
                    continue

                add_marks(student_id, subject_id, marks)

            except ValueError:
                print("Please enter valid numeric values.")

        elif choice == "5":
            view_results()

        elif choice == "6":
            print("Thank you for using GradeSync!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()