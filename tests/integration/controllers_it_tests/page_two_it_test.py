import pytest
from unittest.mock import MagicMock, patch
from flask import url_for
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for page rendering
def test_page_two_render(client):

    response = client.get('/PageTwoDigitalSkills')
    assert response.status_code == 200
    assert b'PageTwoDigitalSkills' in response.data

# Test for valid data submission
def test_page_two_valid_submission(client, monkeypatch):

    # Mock session
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock database connection and operations
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    monkeypatch.setattr('db_connector.create_connection', lambda: mock_conn)
    monkeypatch.setattr('db_connector.close_connection', lambda conn: None)

    # Mock the upsert_multiple_answers function
    mock_upsert_multiple = MagicMock()
    monkeypatch.setattr('daos.upsert_data_multiple.upsert_multiple_answers', mock_upsert_multiple)

    # Mock mappings
    answer_map = {
        'q1': {'valid_option_1': 'Mapped Option 1'},
        'q2': {'valid_option_2': 'Mapped Option 2'},
        # Add other mappings as required
    }
    monkeypatch.setattr('controllers.utils.mappings_page_two.answer_map_page_two_q1', answer_map['q1'])
    monkeypatch.setattr('controllers.utils.mappings_page_two.answer_map_page_two_q2', answer_map['q2'])

    # Submit valid data
    response = client.post('/PageTwoDigitalSkills', data={
        'page-two-question-one': ['valid_option_1'],
        'page-two-question-two': ['valid_option_2']
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location == url_for('page_two.page_two_digital_skills', _external=False)

# Test for missing session
def test_page_two_missing_session(client):

    response = client.post('/PageTwoDigitalSkills', data={
        'page-two-question-one': ['option1']
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location == url_for('login.login', _external=False)

# Test for invalid data submission
def test_page_two_invalid_submission(client, monkeypatch):

    # Mock session
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock mappings with limited valid options
    monkeypatch.setattr('controllers.utils.mappings_page_two.answer_map_page_two_q1', {'valid_option_1': 'Mapped Option 1'})

    # Submit invalid data
    response = client.post('/PageTwoDigitalSkills', data={
        'page-two-question-one': ['invalid_option']
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location == url_for('page_two.page_two_digital_skills', _external=False)

# Test for database connection failure
def test_page_two_db_connector_failure(client, monkeypatch):

    # Mock session
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Mock database connection to return None
    monkeypatch.setattr('db_connector.create_connection', lambda: None)

    response = client.post('/PageTwoDigitalSkills', data={
        'page-two-question-one': ['valid_option']
    }, follow_redirects=False)

    assert response.status_code == 302
    assert response.location == url_for('page_two.page_two_digital_skills', _external=False)