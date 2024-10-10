# test_db_connection.py

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='192.168.1.188',
            user='root',
            password='.20Un123QL!',
            database='individual_project'
        )
        if conn.is_connected():
            print("Connection successfully created")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(conn):
    try:
        if conn.is_connected():
            conn.close()
            print("Connection closed.")
    except NameError:
        print("Connection was never established")

def test_insert_user():
    conn = create_connection()
    if conn:
        my_cursor = conn.cursor()
        try:
            # Insert a new user into the user table
            insert_query = """
            INSERT INTO user (username, userpassword, useremail) 
            VALUES (%s, %s, %s)
            """
            user_data = ("test_user", b"password123", "test_user@example.com")
            my_cursor.execute(insert_query, user_data)
            conn.commit()
            print("User inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            my_cursor.close()
            close_connection(conn)

if __name__ == "__main__":
    test_insert_user()
