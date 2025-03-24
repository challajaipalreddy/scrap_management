import mysql.connector
from config import DB_CONFIG

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as error:
        print(f"Failed to connect to database: {error}")
        return None

def test_connection():
    connection = get_connection()
    if connection and connection.is_connected():
        print("Successfully connected to MySQL database!")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"Connected to database: {db_name}")
        cursor.close()
        connection.close()
        print("Connection closed.")
    else:
        print("Failed to connect to database.")