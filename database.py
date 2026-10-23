import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database="gradesync_db"
    )
    return connection