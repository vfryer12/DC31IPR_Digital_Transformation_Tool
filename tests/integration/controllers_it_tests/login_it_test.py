import pytest
from unittest.mock import MagicMock
from app import create_app
from unittest.mock import MagicMock

@pytest.fixture
def client():

    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client

def test_login_page_render(client):

    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

def test_login_success(client, monkeypatch):

    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for successful login
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None
        elif "SELECT * FROM user WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s" in query:
            return None 
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.side_effect = [
        ("testuser100", "encrypted_password", "testuser@example.com"),
        ("testuser100", "password123", "testuser@example.com"),
    ]

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'testuser100',
        'password': 'password123'
    }, follow_redirects=True)

    # Ensure the response redirects to the index page
    assert response.status_code == 200

def test_login_invalid_username(client, monkeypatch):

    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for invalid username
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.return_value = None

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'nonexistent_user',
        'password': 'password123'
    }, follow_redirects=True)

    # Ensure the response redirects back to the login page with an error message
    assert response.status_code == 200

def test_login_invalid_password(client, monkeypatch):

    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Mock execute and fetchone for valid username but incorrect password
    def mock_execute(query, params):
        if "SELECT * FROM user WHERE username = %s" in query:
            return None
        elif "SELECT * FROM user WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s" in query:
            return None
    mock_cursor.execute.side_effect = mock_execute
    mock_cursor.fetchone.side_effect = [
        ("testuser100", "encrypted_password", "testuser@example.com"),
        None
    ]

    # Simulate sending a POST request to the login page
    response = client.post('/login', data={
        'username': 'testuser100',
        'password': 'wrongpassword'
    }, follow_redirects=True)

    # Ensure the response redirects back to the login page with an error message
    assert response.status_code == 200