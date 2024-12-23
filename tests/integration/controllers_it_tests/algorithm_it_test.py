# algorithm_it_test.py

import pytest
from unittest.mock import MagicMock
from app import create_app

@pytest.fixture
def client():
    """
    Create a test client for the Flask application.
    """
    app = create_app()
    # Set testing mode to True for isolated tests
    app.config['TESTING'] = True
    # Disable CSRF for testing purposes
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        yield client

def test_submit_page_render(client):
    """
    Test if the SubmitAssessmentPage is rendered correctly.
    """
    # Access the SubmitAssessmentPage
    response = client.get('/SubmitAssessmentPage')
    # Ensure the page loads successfully
    assert response.status_code == 200
    # Check if the "Thank You" text is present
    assert b'Thank You' in response.data
    # Check if the form is present
    assert b'<form action="/calculate_score" method="get">' in response.data


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
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)
    
    # Mock the database query result
    # Simulate two records with weights 18 and 18
    mock_cursor.fetchall.return_value = [(1, 18), (2, 18)]
    
    # Simulate a logged-in user by setting session data
    with client.session_transaction() as session:
        # Simulate a logged-in user
        session['user_id'] = 1
    
    # Simulate a GET request to /calculate_score endpoint
    response = client.get('/calculate_score')
    
    # Output the response data for debugging
    # This will show what the response looks like
    print(response.data)
    
    # Check if the response is correct
    assert response.status_code == 200

# Negative Tests

def test_submit_page_invalid_route(client):
    """
    Test accessing an invalid route.
    """
    # Access a non-existent route
    response = client.get('/InvalidRoute')
    # Ensure the server returns a 404 error
    assert response.status_code == 404

def test_calculate_score_without_session(client):
    """
    Test submitting the form without a valid session (user not logged in).
    """
    # Simulate form submission without session
    response = client.get('/calculate_score')
    # Ensure the server returns a 400 error
    assert response.status_code == 400
     # Verify the error message
    assert response.json['error'] == "User not logged in"

def test_calculate_score_with_invalid_method(client):
    """
    Test submitting the form with an invalid HTTP method (e.g., GET instead of POST).
    """
    # Attempt to access the POST endpoint with GET
    response = client.post('/calculate_score')
    # Ensure the server returns a 405 Method Not Allowed error
    assert response.status_code == 405

def test_calculate_score_with_malformed_request(client):
    """
    Test submitting the form with a malformed request payload.
    """
    # Send invalid data
    response = client.get('/calculate_score', data="malformed data")
    # Ensure the server returns a 400 Bad Request error
    assert response.status_code == 400