# login_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db_connection import create_connection, close_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        print("Form submitted!")  # Debugging line
        username = request.form['username']
        password = request.form['password']
        
        # Let's print the username and password for additional debugging
        print(f"Username: {username}, Password: {password}")

        # Simulating successful login for debugging purposes
        session['username'] = username
        flash('Login successful', 'success')
        return redirect(url_for('index'))

    return render_template('LoginPage.html')

# @login_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         print(f"Username: {username}, Password: {password}")  # Debugging line

#         conn = create_connection()
#         if conn:
#             my_cursor = conn.cursor()

#             try:
#                 my_cursor.execute("SELECT * FROM user WHERE username = %s AND userpassword = %s", (username, password))
#                 user = my_cursor.fetchone()

#                 if user:
#                     session['username'] = username
#                     flash('Login successful!', 'success')
#                     return redirect(url_for('index'))
#                 else:
#                     flash('Login failed. Check your username and password.', 'danger')
#                     return redirect(url_for('login.login'))

#             except Exception as e:
#                 flash(f'Error: {e}', 'danger')

#             finally:
#                 my_cursor.close()
#                 close_connection(conn)

#         return redirect(url_for('login.login'))

#     return render_template('LoginPage.html')