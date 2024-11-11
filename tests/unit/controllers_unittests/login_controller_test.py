import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_testing import TestCase

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from controllers.login_controller import login_bp

class LoginTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__, template_folder='templates')
        app.secret_key = 'test_secret_key'
        app.register_blueprint(login_bp)
        return app

    def setUp(self):
        self.client = self.app.test_client()

    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    @patch('controllers.login_controller.create_connection')
    def test_login_success(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.side_effect = [
            {'username': 'test_user'},  # First query result
            {'username': 'test_user'}   # Second query result
        ]
        mock_create_connection.return_value = mock_conn

        response = self.client.post('/login', data=dict(
            username='test_user',
            password='correct_password'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful!', response.data)

    @patch('controllers.login_controller.create_connection')
    def test_login_wrong_password(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.side_effect = [
            {'username': 'test_user'},  # First query result
            None  # Second query result (wrong password)
        ]
        mock_create_connection.return_value = mock_conn

        response = self.client.post('/login', data=dict(
            username='test_user',
            password='wrong_password'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password incorrect', response.data)

    @patch('controllers.login_controller.create_connection')
    def test_login_user_not_found(self, mock_create_connection):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchone.return_value = None  # No user found
        mock_create_connection.return_value = mock_conn

        response = self.client.post('/login', data=dict(
            username='non_existent_user',
            password='password'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username not found', response.data)

if __name__ == '__main__':
    unittest.main()