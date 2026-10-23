from database import create_connection


def add_marks(student_id, subject_id, marks):
    # Validate marks
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return

    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO marks (student_id, subject_id, marks)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (student_id, subject_id, marks))
        connection.commit()

        print("Marks added successfully!")

    except Exception as error:
        if connection is not None:
            connection.rollback()
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def view_results():
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                s.student_id,
                s.student_name,
                SUM(m.marks) AS total_marks,
                AVG(m.marks) AS average_marks,
                COUNT(m.subject_id) AS subject_count,
                MIN(m.marks) AS minimum_marks
            FROM students s
            JOIN marks m ON s.student_id = m.student_id
            GROUP BY s.student_id, s.student_name
            ORDER BY s.student_id
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\n--- Student Results ---")

        if not results:
            print("No student results found.")
            return

        for student in results:
            student_id, name, total, average, count, minimum = student

            # Check whether the student has marks for at least 3 subjects
            if count < 3:
                print(f"ID: {student_id} | Name: {name}: Incomplete result")
                continue

            # Determine pass or fail
            if minimum < 40:
                result = "Fail"
            else:
                result = "Pass"

            # Calculate grade based on average marks
            average = float(average)

            if average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 40:
                grade = "D"
            else:
                grade = "F"

            print(
                f"ID: {student_id} | "
                f"Name: {name} | "
                f"Total: {total} | "
                f"Average: {average:.2f} | "
                f"Grade: {grade} | "
                f"Result: {result}"
            )

    except Exception as error:
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()