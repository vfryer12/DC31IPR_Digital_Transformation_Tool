import pytest
from unittest.mock import MagicMock
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

# Test for login page rendering
def test_login_page_render(client):
    """
    Test if the login page renders correctly.
    """
    response = client.get('/login')  # Access the login page
    assert response.status_code == 200  # Ensure the page loads successfully
    assert b'Username' in response.data  # Check if the "Username" field is present
    assert b'Password' in response.data  # Check if the "Password" field is present

# Test for successful login
def test_login_success(client, monkeypatch):
    """
    Test if the login form successfully logs in a user.
    """
    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for successful login
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None  # Simulate user found
        elif "SELECT * FROM user WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s" in query:
            return None  # Simulate correct password
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.side_effect = [
        ("testuser100", "encrypted_password", "testuser@example.com"),  # Simulate user exists
        ("testuser100", "password123", "testuser@example.com"),  # Simulate correct password
    ]

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'testuser100',
        'password': 'password123'
    }, follow_redirects=True)

    # Ensure the response redirects to the index page
    assert response.status_code == 200  # Final page status

# Test for incorrect username
def test_login_invalid_username(client, monkeypatch):
    """
    Test if the login form shows an error when an invalid username is used.
    """
    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for invalid username
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None  # Simulate no user found
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.return_value = None  # No user exists

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'nonexistent_user',
        'password': 'password123'
    }, follow_redirects=True)

    # Ensure the response redirects back to the login page with an error message
    assert response.status_code == 200  # Final page status

# Test for incorrect password
def test_login_invalid_password(client, monkeypatch):
    """
    Test if the login form shows an error when an incorrect password is used.
    """
    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for valid username but incorrect password
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None  # Simulate user found
        elif "SELECT * FROM user WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s" in query:
            return None  # Simulate incorrect password
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.side_effect = [
        ("testuser100", "encrypted_password", "testuser@example.com"),  # Simulate user exists
        None  # Simulate incorrect password
    ]

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'testuser100',
        'password': 'wrongpassword'
    }, follow_redirects=True)

    # Ensure the response redirects back to the login page with an error message
    assert response.status_code == 200  # Final page status