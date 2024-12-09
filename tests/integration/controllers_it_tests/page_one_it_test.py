import pytest
from unittest.mock import MagicMock, call
from flask import url_for, session
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for page rendering
def test_page_one_render(client):
    """
    Test if the PageOneDigitalStrategy page renders correctly.
    """
    response = client.get('/PageOneDigitalStrategy')
    assert response.status_code == 200  # Ensure the page loads successfully
    assert b'PageOneDigitalStrategy' in response.data  # Ensure the page header or unique identifier is present

def test_page_one_valid_submission(client, monkeypatch):
    """
    Test if the form submission processes valid data successfully.
    """
    # Mock the session
    with client.session_transaction() as sess:
        sess['user_id'] = 1
    
    # Mock database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)
    monkeypatch.setattr('db_connection.close_connection', lambda conn: None)
    
    # Mock the upsert operations
    mock_upsert_single = MagicMock()
    mock_upsert_multiple = MagicMock()
    monkeypatch.setattr('daos.upsert_data_single.upsert_single_answer', mock_upsert_single)
    monkeypatch.setattr('daos.upsert_data_multiple.upsert_multiple_answers', mock_upsert_multiple)
    
    # Mock answer mappings
    answer_map_q1 = {'1': 'No plan in place', '2': 'Needs Improvement', '3': 'Fully Aligned'}
    answer_map_q2 = {'cio': 'Chief Information Officer (CIO)', 'cto': 'Chief Technology Officer (CTO)', 'dtm': 'Digital Transformation Manager', 'cdo': 'Chief Digital Officer (CDO)', 'itd': 'IT Director/Manager', 'bul': 'Business Unit Leader', 'md': 'Marketing Director', 'dal': 'Data Analytics Leader', 'other': 'Other'}
    answer_map_q3 = {'never': 'Never', 'monthly': 'Every Month', 'quarterly': 'Quarterly', 'year': 'Annual', 'continuous': 'Continuous'}
    answer_map_q4 = {'return-on-investment-answer': 'Return on Investment (ROI)', 'conversion-rates-answer': 'Conversion Rates', 'customer-acquisition-cost-and-customer-lifetime-value-answer': 'Customer Acquisition Cost (CAC) and Customer Lifetime Value (CLV)', 'website-traffic-answer': 'Website Traffic', 'customer-engagement-answer': 'Customer Engagement', 'social-media-metrics-and-email-marketing-metrics-answer': 'Social Media Metrics and Email Marketing Metrics', 'seo-rankings-answer': 'SEO Rankings'}
    
    monkeypatch.setattr('controllers.utils.mappings_page_one.answer_map_q1', answer_map_q1)
    monkeypatch.setattr('controllers.utils.mappings_page_one.answer_map_q2', answer_map_q2)
    monkeypatch.setattr('controllers.utils.mappings_page_one.answer_map_q3', answer_map_q3)
    monkeypatch.setattr('controllers.utils.mappings_page_one.answer_map_q4', answer_map_q4)
    
    # Simulate a POST request with updated data matching the expected keys
    response = client.post('/PageOneDigitalStrategy', data={
        'question-one': '1',  # Using '1' for the answer key for question one
        'question-two': 'cio',  # Correct key for CIO role
        'question-three': 'never',  # Correct key for frequency
        'question-four': ['return-on-investment-answer'],  # Correct key for ROI
    }, follow_redirects=True)

    # Debugging output
    print("Response status:", response.status_code)
    print("Mock upsert_single calls:", mock_upsert_single.mock_calls)
    print("Mock upsert_multiple calls:", mock_upsert_multiple.mock_calls)
    
    # Ensure no validation errors
    assert response.status_code == 200  # Ensure final status is OK

# Test for missing session
def test_page_one_missing_session(client):
    """
    Test if the user is redirected to login when session is missing.
    """

    response = client.post('/PageOneDigitalStrategy', data={
        'question-one': 'option1',
        'question-two': 'option2'
    }, follow_redirects=False)

    assert response.status_code == 302  # Ensure redirection
    assert response.location == '/login'  # Expect relative URL

# Test for invalid data submission
def test_page_one_invalid_submission(client, monkeypatch):
    """
    Test if invalid form submissions are handled correctly.
    """
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock database connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connection.create_connection', lambda: mock_conn)
    monkeypatch.setattr('db_connection.close_connection', lambda conn: None)

    # Mock answer mappings with missing data
    monkeypatch.setattr('controllers.utils.mappings_page_one.answer_map_q1', {'valid_option': 'mapped_valid_option'})

    # Simulate a POST request with invalid data
    response = client.post('/PageOneDigitalStrategy', data={
        'question-one': 'invalid_option',  # Invalid option not in mapping
    }, follow_redirects=False)

    assert response.status_code == 302  # Ensure redirection
    assert response.location == '/PageOneDigitalStrategy'

# Test for database connection failure
def test_page_one_db_connection_failure(client, monkeypatch):
    """
    Test if database connection failure is handled correctly.
    """
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock database connection failure
    monkeypatch.setattr('db_connection.create_connection', lambda: None)

    response = client.post('/PageOneDigitalStrategy', data={
        'question-one': 'option1',
        'question-two': 'option2'
    }, follow_redirects=False)

    assert response.status_code == 302  # Ensure redirection
    assert response.location == '/PageOneDigitalStrategy'