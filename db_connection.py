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

# main_script.py (or any other module)

# from db_connection import create_connection, close_connection

# conn = create_connection()
# if conn:
#     my_cursor = conn.cursor()
#     # Your SQL operations here
#     conn.commit()
#     close_connection(conn)
# else:
#     print("Failed to create connection.")

