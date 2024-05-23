from flask import Flask, request
import pymysql.cursors

from utils.password_handler import verify_password

app = Flask(__name__)

@app.route('/submit-login', methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['password']

    connection = pymysql.connect(host='localhost',
                                 user='your_username',
                                 password='your_password',
                                 db='user',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `username`=%s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            if result:
                salt = result['salt']
                key = result['key']
                if verify_password(salt, key, password):
                    return "User logged in successfully!"
                else:
                    return "Invalid username or password!"
            else:
                return "Invalid username or password!"
    finally:
        connection.close()