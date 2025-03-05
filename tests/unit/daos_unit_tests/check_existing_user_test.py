import pytest
from unittest.mock import MagicMock
from daos.check_existing_user import check_existing_user

@pytest.fixture
def mock_cursor():

    return MagicMock()


def test_check_existing_user_found_by_username(mock_cursor):
    # Simulate the result of the query for an existing user
    mock_cursor.fetchone.return_value = ('1', 'john_doe', 'john@example.com')

    username = 'john_doe'
    email = 'john@example.com'

    result = check_existing_user(mock_cursor, username, email)

    # Assert the query is executed with the right parameters
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM user WHERE username = %s OR useremail = %s", 
        (username, email)
    )
    
    # Assert the result returned matches the mock data
    assert result == ('1', 'john_doe', 'john@example.com')


def test_check_existing_user_found_by_email(mock_cursor):
    # Simulate the result of the query for an existing user by email
    mock_cursor.fetchone.return_value = ('2', 'jane_doe', 'jane@example.com')

    username = 'not_jane'
    email = 'jane@example.com'

    result = check_existing_user(mock_cursor, username, email)

    # Assert the query is executed with the correct parameters
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM user WHERE username = %s OR useremail = %s", 
        (username, email)
    )

    # Assert the result returned matches the mock data
    assert result == ('2', 'jane_doe', 'jane@example.com')


def test_check_existing_user_not_found(mock_cursor):
    # Simulate that no user is found
    mock_cursor.fetchone.return_value = None

    username = 'non_existing_user'
    email = 'non_existing@example.com'

    result = check_existing_user(mock_cursor, username, email)

    # Assert the query is executed with the correct parameters
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM user WHERE username = %s OR useremail = %s", 
        (username, email)
    )

    # Assert the result is None as no user is found
    assert result is None


def test_check_existing_user_query_execution(mock_cursor):
    # No need to simulate a result, just check the query execution
    username = 'john_doe'
    email = 'john@example.com'

    check_existing_user(mock_cursor, username, email)

    # Assert that the query is called with the correct parameters
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM user WHERE username = %s OR useremail = %s", 
        (username, email)
    )
