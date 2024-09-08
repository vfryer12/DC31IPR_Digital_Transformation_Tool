from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize the Flask app and specify the template folder
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:.20Un123QL!@192.168.1.188/individual_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from controllers.login import login_bp
from controllers.register import register_bp

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)

@app.route('/')
def index():
    return redirect(url_for('login.login'))