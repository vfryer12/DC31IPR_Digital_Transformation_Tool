from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db_connection import create_connection, close_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = create_connection()
        if conn:
            my_cursor = conn.cursor()

            try:
                my_cursor.execute("SELECT * FROM user WHERE username = %s AND userpassword = %s", (username, password))
                user = my_cursor.fetchone()

                if user:
                    session['username'] = username
                    flash('Login successful!', 'success')
                    return redirect(url_for('index'))  # Redirect to a different page after login
                else:
                    flash('Login failed. Check your username and password.', 'danger')
                    return redirect(url_for('index'))  # Redirect back to login page

            except Exception as e:
                flash(f'Error: {e}', 'danger')

            finally:
                my_cursor.close()
                close_connection(conn)

        return redirect(url_for('index'))

    return render_template('LoginPage.html')  # Serve login page on GET request

@login_bp.route('/register')
def register():
    return "Registration page not implemented yet."  # Placeholder for registration page
