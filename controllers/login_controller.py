# login_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db_connection import create_connection, close_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Debugging line
        print(f"Username from form: {username}, Password from form: {password}")

        conn = create_connection()
        if conn:
            print("Connection established")
            my_cursor = conn.cursor()

            try:
                print("Executing query")
                query = "SELECT * FROM user WHERE username = %s"
                my_cursor.execute(query, (username,))
                user = my_cursor.fetchone()

                if user:
                    # Check password
                    query = "SELECT * FROM user WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s"
                    my_cursor.execute(query, (username, password))
                    user = my_cursor.fetchone()

                    if user:
                        print("User found")
                        session['username'] = username
                        flash('Login successful!', 'success')
                        # Redirect to home page after login
                        return redirect(url_for('index'))
                    else:
                        print("Password incorrect")
                        flash('Password incorrect. Please try again.', 'danger')
                        return redirect(url_for('login.login'))

                else:
                    print("Username not found")
                    flash('Username not found. Please try again or register.', 'danger')
                    return redirect(url_for('login.login'))

            except Exception as e:
                print(f"Error executing query: {e}")
                flash(f'Error: {e}', 'danger')

            finally:
                my_cursor.close()
                close_connection(conn)

        else:
            print("Failed to establish database connection")
            flash('Database connection failed.', 'danger')
            return redirect(url_for('login.login'))

    return render_template('LoginPage.html')