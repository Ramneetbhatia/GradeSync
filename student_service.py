from database import create_connection


def add_student(student_id, student_name, email):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO students (student_id, student_name, email)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (student_id, student_name, email))
        connection.commit()
        print("Student added successfully!")

    except Exception as error:
        if connection is not None:
            connection.rollback()
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def view_students():
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students ORDER BY student_id"
        )
        students = cursor.fetchall()

        print("\n--- Student Records ---")
        for student in students:
            print(student)

    except Exception as error:
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


def search_student(student_id):
    connection = None
    cursor = None

    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        if student:
            print("Student found:", student)
        else:
            print("Student not found.")

    except Exception as error:
        print("Error:", error)

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()