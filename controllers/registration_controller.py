from flask import Blueprint, render_template, request, redirect, url_for, flash
from db_connector import create_connection, close_connection
from models.login_model import LoginModel
from daos.check_existing_user import check_existing_user
from daos.insert_new_user import insert_new_user

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/registration', methods=['POST'])
def register():
    login_model = LoginModel()

    if request.method == 'POST':
        login_model.username = request.form['username']
        login_model.password = request.form['pwd']
        email = request.form['email']

        conn = create_connection()
        if conn:
            my_cursor = conn.cursor()

            try:
                existing_user = check_existing_user(my_cursor, login_model.username, email)
                if existing_user:
                    flash('Username or email already exists. Please choose another.', 'danger')
                    return redirect(url_for('registration.register'))

                # Encrypt the password before inserting
                insert_new_user(my_cursor, login_model.username, login_model.password, email)
                conn.commit()
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('login.login'))

            except Exception as e:
                flash(f'Error: {e}', 'danger')

            finally:
                my_cursor.close()
                close_connection(conn)

        else:
            flash('Database connection failed.', 'danger')
            return redirect(url_for('registration.register'))
        
    # Render the login page with an empty model
    return render_template('RegistrationPage.html', login_model=login_model)