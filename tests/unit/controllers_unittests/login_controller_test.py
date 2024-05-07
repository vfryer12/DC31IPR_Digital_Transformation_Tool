import unittest
from unittest.mock import patch, MagicMock
from flask import request
from controllers.login_controller import app
from controllers.utils.password_handler import verify_password

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('pymysql.connect')
    def test_login_success(self, mock_sql):
        # Mock the MySQL connection
        mock_cursor = MagicMock()
        mock_sql.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock the fetchone result
        mock_cursor.fetchone.return_value = {
            'salt': b'somesalt',
            'key': verify_password(b'somesalt', 'password')[1]
        }

        # Send a POST request to the /submit-login route
        response = self.app.post('/submit-login', data={'username': 'test', 'password': 'password'})

        # Check the response data
        self.assertEqual(response.data, b'User logged in successfully!')

    @patch('pymysql.connect')
    def test_login_failure(self, mock_sql):
        # Mock the MySQL connection
        mock_cursor = MagicMock()
        mock_sql.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        # Mock the fetchone result
        mock_cursor.fetchone.return_value = None

        # Send a POST request to the /submit-login route
        response = self.app.post('/submit-login', data={'username': 'test', 'password': 'wrongpassword'})

        # Check the response data
        self.assertEqual(response.data, b'Invalid username or password')

if __name__ == '__main__':
    unittest.main()