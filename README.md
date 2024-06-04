# DC31IPR_Digital_Transformation_Tool
An all-encompassing tool designed to aid organisations in evaluating their digital maturity.

# How to run

# Installation Information

This guide will help you get started.


## Prerequisites

Before you start make sure you have Python installed on your system. If not you can download it from the official Python website.


## Installation

The software is packaged and distributed using Poetry. To install the software, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where you downloaded our software.

3. Run the following command to install the software and its dependencies:

poetry install


## Running the Software

To run the software, use the following command in your terminal or command prompt:

poetry run <name-of-the-main-script>

Replace <name-of-the-main-script> with the actual name of the main script of the software.

Final step: poetry install


## Flask password protection

Flask is a lightweight Python web framework.

An instance of the Flask application is created with app = Flask(__name__). This instance represents the web application and all its functionalities.

A route for login is then defined using @app.route('/submit-login', methods=['POST']). This tells Flask which function should run when a user navigates to a specific URL. In this case the login page.

When a user submits the login form, Flask’s request.form is used to retrieve the username and password from the form data.

Before storing the password in a database, the password is hashed using a library like hashlib. This transforms the password into a fixed-length sequence of bytes adding a layer of security.

When a user logs in the entered password is hashed and compared to the stored hash. If the hashes match, the password is verified

## Using Python Server

python -m http.server 8080

http://localhost:8080/views/HomePage.html
