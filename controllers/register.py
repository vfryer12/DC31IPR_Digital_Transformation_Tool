from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.users import User
from controllers import bcrypt

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        User.add_user(username, hashed_password, email)
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login.login'))
    return render_template('RegistrationPage.html')