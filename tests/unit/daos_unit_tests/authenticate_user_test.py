import pytest
from unittest.mock import MagicMock
from daos.authenticate_user import authenticate_user

@pytest.fixture
def mock_cursor():

    return MagicMock()

def test_authenticate_user_positive(mock_cursor):
    mock_cursor.fetchone.return_value = {"id": 1, "username": "test_user", "password": "encrypted_password"}
    
    # Call the DAO function
    username = "test_user"
    password = "correct_password"
    result = authenticate_user(mock_cursor, username, password)
    
    # Assertions
    mock_cursor.execute.assert_called_once_with(
        """
            SELECT * FROM user
            WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s
        """,
        (username, password)
    )
    assert result == {"id": 1, "username": "test_user", "password": "encrypted_password"}

def test_authenticate_user_negative(mock_cursor):
    # Simulates authentication failure
    mock_cursor.fetchone.return_value = None
    
    # Call the DAO function
    username = "test_user"
    password = "wrong_password"
    result = authenticate_user(mock_cursor, username, password)
    
    # Assertions
    mock_cursor.execute.assert_called_once_with(
        """
            SELECT * FROM user
            WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s
        """,
        (username, password)
    )
    assert result is None