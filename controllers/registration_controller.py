# registration_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from db_connection import create_connection, close_connection

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        email = request.form['email']

        conn = create_connection()
        if conn:
            my_cursor = conn.cursor()

            try:
                # Check if username or email already exists
                my_cursor.execute("SELECT * FROM user WHERE username = %s OR useremail = %s", (username, email))
                existing_user = my_cursor.fetchone()

                if existing_user:
                    flash('Username or email already exists. Please choose another.', 'danger')
                    return redirect(url_for('registration.register'))

                # Encrypt the password before inserting
                encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
                insert_query = f"""
                INSERT INTO user (username, userpassword, useremail) 
                VALUES (%s, {encrypted_password_query}, %s)
                """
                user_data = (username, password, email)
                my_cursor.execute(insert_query, user_data)
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

    return render_template('RegistrationPage.html')