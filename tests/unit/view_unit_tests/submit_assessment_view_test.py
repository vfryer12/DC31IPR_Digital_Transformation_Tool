import pytest
from unittest.mock import MagicMock

# Import your create_app function from the main application file
from app import create_app

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

def test_submit_page_render(client):
    """
    Test if the SubmitAssessmentPage is rendered correctly.
    """
    response = client.get('/SubmitAssessmentPage')  # Access the SubmitAssessmentPage
    assert response.status_code == 200  # Ensure the page loads successfully
    assert b'Thank You' in response.data  # Check if the "Thank You" text is present
    assert b'<form action="/calculate_score" method="get">' in response.data  # Check if the form is present


def test_submit_page_get(client, monkeypatch):
    """
    Test the submission of the form to the /calculate_score endpoint.
    """
    
    # Mock the response of the calculate_score endpoint
    def mock_calculate_score():
        return {"total_score": 18, "feedback": "Score is within the happy path: Keep up the good work!"}
    
    # Replace the actual calculate_score function with the mock
    monkeypatch.setattr(
        'controllers.algorithm_controller.calculate_score', mock_calculate_score
    )
    
    # Mock the database call (create_connection and its methods)
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)
    
    # Mock the database query result
    mock_cursor.fetchall.return_value = [(1, 18), (2, 18)]  # Simulate two records with weights 18 and 18
    
    # Simulate a logged-in user by setting session data
    with client.session_transaction() as session:
        session['user_id'] = 1  # Simulate a logged-in user
    
    # Simulate a GET request to /calculate_score endpoint
    response = client.get('/calculate_score')  # Simulate form submission with GET
    
    # Output the response data for debugging
    print(response.data)  # This will show what the response looks like
    
    # Check if the response is correct
    assert response.status_code == 200  # Ensure th

# Negative Tests

def test_submit_page_invalid_route(client):
    """
    Test accessing an invalid route.
    """
    response = client.get('/InvalidRoute')  # Access a non-existent route
    assert response.status_code == 404  # Ensure the server returns a 404 error

def test_calculate_score_without_session(client):
    """
    Test submitting the form without a valid session (user not logged in).
    """
    response = client.get('/calculate_score')  # Simulate form submission without session
    assert response.status_code == 400  # Ensure the server returns a 400 error
    assert response.json['error'] == "User not logged in"  # Verify the error message

def test_calculate_score_with_invalid_method(client):
    """
    Test submitting the form with an invalid HTTP method (e.g., GET instead of POST).
    """
    response = client.post('/calculate_score')  # Attempt to access the POST endpoint with GET
    assert response.status_code == 405  # Ensure the server returns a 405 Method Not Allowed error

def test_calculate_score_with_malformed_request(client):
    """
    Test submitting the form with a malformed request payload.
    """
    response = client.get('/calculate_score', data="malformed data")  # Send invalid data
    assert response.status_code == 400  # Ensure the server returns a 400 Bad Request error