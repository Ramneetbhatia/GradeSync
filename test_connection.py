from database import create_connection

connection = create_connection()

if connection.is_connected():
    print("Connected to MySQL successfully!")

connection.close()