import pytest
from unittest.mock import MagicMock
from daos.insert_new_user import insert_new_user

@pytest.fixture
def mock_cursor():
    """Fixture to create a mock cursor."""
    return MagicMock()

def test_insert_new_user(mock_cursor):
    username = 'testuser'
    password = 'testpassword'
    email = 'testuser@example.com'
    
    # Call the function being tested
    insert_new_user(mock_cursor, username, password, email)

    # Prepare the expected query and arguments
    encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, {encrypted_password_query}, %s)
    """
    
    # Verify cursor.execute was called with the correct SQL query and parameters
    mock_cursor.execute.assert_called_once_with(
        query, 
        (username, password, email)
    )

def test_insert_new_user_with_empty_password(mock_cursor):
    username = 'testuser'
    password = ''
    email = 'testuser@example.com'

    # Call the function with an empty password
    insert_new_user(mock_cursor, username, password, email)

    # Prepare the expected query and arguments
    encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, {encrypted_password_query}, %s)
    """
    
    # Verify cursor.execute was called with the correct SQL query and parameters
    mock_cursor.execute.assert_called_once_with(
        query, 
        (username, password, email)
    )

def test_insert_new_user_with_special_characters(mock_cursor):
    username = 'testuser!@#'
    password = 'password$%^'
    email = 'testuser@example.com'

    # Call the function with special characters in the username and password
    insert_new_user(mock_cursor, username, password, email)

    # Prepare the expected query and arguments
    encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, {encrypted_password_query}, %s)
    """
    
    # Verify cursor.execute was called with the correct SQL query and parameters
    mock_cursor.execute.assert_called_once_with(
        query, 
        (username, password, email)
    )

def test_insert_new_user_check_query_format(mock_cursor):
    username = 'testuser'
    password = 'testpassword'
    email = 'testuser@example.com'

    # Call the function being tested
    insert_new_user(mock_cursor, username, password, email)

    # Ensure the query contains AES_ENCRYPT function with password
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, AES_ENCRYPT(%s, 'encryption_key'), %s)
    """

    # Check that the query format includes the expected encryption query
    assert "AES_ENCRYPT(%s, 'encryption_key')" in query
    mock_cursor.execute.assert_called_once_with(
        query, 
        (username, password, email)
    )