import pytest
from unittest.mock import MagicMock
from flask import session

@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_four_render(client):
    """
    Test if the PageFourMarketTrends page renders correctly.
    """
    response = client.get('/PageFourMarketTrends')
    assert response.status_code == 200
    assert b'PageFourMarketTrends' in response.data  # Ensure unique identifier

def test_page_four_valid_submission(client, monkeypatch):
    """
    Test valid data submission and successful processing.
    """
    # Mock the session
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock database connection and operations
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)
    monkeypatch.setattr('db_connection.close_connection', lambda conn: None)

    # Mock answer mappings
    answer_map_page_four_q1 = {'1': 'Option 1'}
    answer_map_page_four_q2 = {'2': 'Option 2'}
    monkeypatch.setattr('controllers.utils.mappings_page_four.answer_map_page_four_q1', answer_map_page_four_q1)
    monkeypatch.setattr('controllers.utils.mappings_page_four.answer_map_page_four_q2', answer_map_page_four_q2)
    
    # Mock upsert function
    mock_upsert_multiple = MagicMock()
    monkeypatch.setattr('daos.upsert_data_multiple.upsert_multiple_answers', mock_upsert_multiple)

    # Simulate valid POST request
    response = client.post('/PageFourMarketTrends', data={
        'page-four-question-one': ['1'],
        'page-four-question-two': ['2'],
    }, follow_redirects=True)

    assert response.status_code == 200

def test_page_four_missing_session(client):
    """
    Test redirection when session is missing.
    """
    response = client.post('/PageFourMarketTrends', data={
        'page-four-question-one': ['1'],
    }, follow_redirects=False)
    assert response.status_code == 302
    assert response.location.endswith('/login')  # Ensure redirection to login

def test_page_four_invalid_submission(client, monkeypatch):
    """
    Test handling of invalid form submissions.
    """
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock mappings with limited options
    monkeypatch.setattr('controllers.utils.mappings_page_four.answer_map_page_four_q1', {'valid_option': 'Mapped Valid Option'})

    # Simulate POST request with invalid data
    response = client.post('/PageFourMarketTrends', data={
        'page-four-question-one': ['invalid_option'],
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location.endswith('/PageFourMarketTrends')  # Redirect to the same page

def test_page_four_db_connection_failure(client, monkeypatch):
    """
    Test handling of database connection failure.
    """
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Simulate database connection failure
    monkeypatch.setattr('db_connection.create_connection', lambda: None)

    response = client.post('/PageFourMarketTrends', data={
        'page-four-question-one': ['1'],
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location.endswith('/PageFourMarketTrends')  # Redirect to the same page
