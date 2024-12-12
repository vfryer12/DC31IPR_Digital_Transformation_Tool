import pytest
from unittest.mock import MagicMock
from daos.find_user_by_username import find_user_by_username

@pytest.fixture
# Mock cursor and its behavior
def mock_cursor():
    """Fixture to create a mock cursor."""
    return MagicMock()

# Positive Test: User exists in the database
def test_find_user_by_username_positive(mock_cursor):
    mock_cursor.fetchone.return_value = {"id": 1, "username": "test_user", "password": "encrypted_password"}
    
    # Call the DAO function
    username = "test_user"
    result = find_user_by_username(mock_cursor, username)
    
    # Assertions
    mock_cursor.execute.assert_called_once_with("SELECT * FROM user WHERE username = %s", (username,))
    assert result == {"id": 1, "username": "test_user", "password": "encrypted_password"}

# Negative Test: User does not exist in the database
def test_find_user_by_username_negative(mock_cursor):
    # Simulates no matching user
    mock_cursor.fetchone.return_value = None
    
    # Call the DAO function
    username = "nonexistent_user"
    result = find_user_by_username(mock_cursor, username)
    
    # Assertions
    mock_cursor.execute.assert_called_once_with("SELECT * FROM user WHERE username = %s", (username,))
    assert result is None
