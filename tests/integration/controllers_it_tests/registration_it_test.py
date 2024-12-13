from flask import url_for
import pytest
from app import create_app
from unittest.mock import MagicMock


@pytest.fixture
def client():
    """
    Create a test client for the Flask application.
    """
    app = create_app()
    app.config['TESTING'] = True  # Set testing mode to True for isolated tests
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing purposes

    with app.test_client() as client:
        yield client

# Test for registration page rendering
def test_registration_page_render(client):
    """
    Test if the registration page renders correctly.
    """
    response = client.get('/registration')  # Access the registration page
    assert response.status_code == 200  # Ensure the page loads successfully
    assert b'Username' in response.data  # Check if the "Username" field is present
    assert b'Password' in response.data  # Check if the "Password" field is present
    assert b'Email' in response.data  # Check if the "Email" field is present

def test_registration_success(client, monkeypatch):
    """
    Test if the registration form successfully creates a new user.
    """
    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Mock execute and fetchone
    def mock_execute(query, params):
        if "INSERT INTO user" in query:
            return None  # Simulate successful insertion
        elif "SELECT * FROM user" in query:
            return None  # Simulate no existing user found
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.return_value = None  # No existing user

    # Simulate sending a POST request to the registration page
    response = client.post('/registration', data={
        'username': 'testuser100',
        'pwd': 'password123',
        'email': 'testuser@example.com'
    }, follow_redirects=True)

    # Validate the final response
    assert response.status_code == 200  # Final page status

# Test for registration with an existing username or email
def test_registration_existing_user(client, monkeypatch):
    """
    Test if the system correctly handles a case where the username or email already exists.
    """
    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Simulate an existing user in the database
    def mock_execute(query, params):
        if "SELECT * FROM user" in query:
            return [("existing_user", "password", "existing@example.com")]  # Simulate existing user
        return None

    mock_cursor.execute = mock_execute

    # Simulate sending a POST request to the registration page
    response = client.post('/registration', data={
        'username': 'existing_user',
        'pwd': 'password123',
        'email': 'existing@example.com'
    })

    # Ensure the response redirects back with a flash message
    assert response.status_code == 302

# Test for invalid database connection
def test_registration_db_error(client, monkeypatch):
    """
    Test if the system handles database connection failure gracefully.
    """
    # Mock the database connection failure
    monkeypatch.setattr('db_connector.create_connection', lambda: None)

    # Simulate sending a POST request to the registration page
    response = client.post('/registration', data={
        'username': 'testuser',
        'fname': 'test',
        'lname': 'user',
        'pwd': 'password123',
        'email': 'testuser@example.com'
    })

    # Ensure the response redirects back with a flash message
    assert response.status_code == 302

# Test for invalid method (GET instead of POST)
def test_registration_invalid_method(client):
    """
    Test accessing the registration page with an invalid method (GET).
    """
    response = client.get('/registration')  # Should be a GET request
    assert response.status_code == 200  # Ensure the registration page renders correctly

# Test for registration with missing form data
def test_registration_missing_data(client):
    """
    Test the registration process with missing form data (e.g., missing username).
    """
    response = client.post('/registration', data={
        'pwd': 'password123',
        'email': 'testuser@example.com'
    })

    # Check if the form submission results in a failure due to missing data
    assert response.status_code == 400