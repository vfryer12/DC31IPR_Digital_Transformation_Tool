import base64
import os
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host='192.168.1.188',
            user=os.environ["PROJECT_USER"],
            password=os.environ["PROJECT_PASSWORD"],
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