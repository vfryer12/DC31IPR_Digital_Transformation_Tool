import pytest
from app import create_app
from unittest.mock import MagicMock


@pytest.fixture
def client():

    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client

# Test for registration page rendering
def test_registration_page_render(client):

    response = client.get('/registration')
    
    assert response.status_code == 200
    assert b'Username' in response.data  
    assert b'Password' in response.data  
    assert b'Email' in response.data  

def test_registration_success(client, monkeypatch):

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

    # Mock the database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)

    # Simulate an existing user in the database
    def mock_execute(query, params):
        if "SELECT * FROM user" in query:
            return [("existing_user", "password", "existing@example.com")]
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

def test_registration_db_error(client, monkeypatch):

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

def test_registration_invalid_method(client):

    response = client.get('/registration')
    assert response.status_code == 200 

# Test for registration with missing form data
def test_registration_missing_data(client):
 
    response = client.post('/registration', data={
        'pwd': 'password123',
        'email': 'testuser@example.com'
    })

    # Check if the form submission results in a failure due to missing data
    assert response.status_code == 400