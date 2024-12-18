import pytest
from unittest.mock import MagicMock
from daos.get_user_answer_weights import get_user_answer_weights

@pytest.fixture
def mock_cursor():
    """Fixture to provide a mock database cursor."""
    return MagicMock()

from textwrap import dedent

def test_get_user_weights(mock_cursor):
    user_id = 1

    # Simulate the result of the query
    mock_cursor.fetchall.return_value = [(1, 10), (2, 15), (3, 20)]

    # Call the DAO function
    weights = get_user_answer_weights(mock_cursor, user_id)

    # Assert the query is executed with the correct parameters
    mock_cursor.execute.assert_called_once_with(
        dedent("""
            SELECT ua.questionsId, a.weighting
            FROM userAnswers ua
            JOIN answers a ON ua.answersId = a.id
            WHERE ua.userId = %s
        """),
        (user_id,)
    )

    # Assert the fetched data is returned correctly
    assert weights == [(1, 10), (2, 15), (3, 20)]

def test_get_user_weights_with_error(mock_cursor):
    user_id = 1

    # Simulate an error during the execution of the query
    mock_cursor.execute.side_effect = Exception("Database connection error")

    # Call the DAO function
    weights = get_user_answer_weights(mock_cursor, user_id)

    # Assert that the result is None due to the error
    assert weights is None
