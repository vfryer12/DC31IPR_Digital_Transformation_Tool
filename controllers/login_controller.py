# login_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db_connector import create_connection, close_connection
from models.login_model import LoginModel
from daos.authenticate_user import authenticate_user
from daos.find_user_by_username import find_user_by_username

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_model = LoginModel()

    if request.method == 'POST':
        login_model.username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        # Debugging line
        print(f"Username from form: {login_model.username}, Password from form: {password}")

        conn = create_connection()
        if conn:
            print("Connection established")
            my_cursor = conn.cursor()

            try:
                print("Executing query")
                # query = "SELECT * FROM user WHERE username = %s"
                # my_cursor.execute(query, (login_model.username,))
                # user = my_cursor.fetchone()
                user = find_user_by_username(my_cursor, login_model.username)
                if user:
                    # Check password
                    authenticated_user = authenticate_user(my_cursor, login_model.username, password)

                    if authenticated_user:
                        print("User found")
                        session['username'] = login_model.username
                        session['user_id'] = user[0]  # Ensure index is correct for user ID
                        print(f"Session data set: user_id={user[0]}, username={login_model.username}")
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

    # Render the login page with an empty model
    return render_template('LoginPage.html', login_model=login_model)
