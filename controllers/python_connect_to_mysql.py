import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='192.168.1.188',
        user='root',
        password='.20Un123QL!',
        database='individual_project'
    )
    if conn.is_connected():
        print("Connection successfully created!")
        my_cursor = conn.cursor()
        # Your SQL operations here
        conn.commit()
except Error as e:
    print(f"Error: {e}")
finally:
    try:
        if conn.is_connected():
            my_cursor.close()
            conn.close()
            print("Connection closed.")
    except NameError:
        print("Connection was never established.")
