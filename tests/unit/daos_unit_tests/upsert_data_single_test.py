import pytest
from unittest.mock import MagicMock
from daos.upsert_data_single import upsert_single_answer


@pytest.fixture
def mock_cursor():

    return MagicMock()


def test_upsert_single_answer_update_existing(mock_cursor):

    answer_value = "Updated Answer"
    question_id = 101
    user_id = 5

    # Mock database responses
    # Simulate the answer ID exists in the answers table
    mock_cursor.fetchone.side_effect = [
        (1,),  # Answer ID for the provided answer
    ]
    # Simulate an existing user answer record
    mock_cursor.fetchall.return_value = [(1,)]

    # Call the function
    upsert_single_answer(mock_cursor, answer_value, question_id, user_id)

    # Verify SELECT query to find the answer ID
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, answer_value)
    )
    
    # Verify SELECT query to check user answers
    mock_cursor.execute.assert_any_call(
        "SELECT answersId FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify the UPDATE query is executed
    mock_cursor.execute.assert_any_call(
        "UPDATE userAnswers SET answersId = %s WHERE userId = %s AND questionsId = %s",
        (1, user_id, question_id)
    )


def test_upsert_single_answer_insert_new(mock_cursor):

    answer_value = "New Answer"
    question_id = 102
    user_id = 6

    # Mock database responses
    # Simulate the answer ID exists in the `answers` table
    mock_cursor.fetchone.side_effect = [
        (2,),  # Answer ID for the provided answer
    ]
    # Simulate no existing user answer records
    mock_cursor.fetchall.return_value = []

    # Call the function
    upsert_single_answer(mock_cursor, answer_value, question_id, user_id)

    # Verify SELECT query to find the answer ID
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, answer_value)
    )
    
    # Verify SELECT query to check user answers
    mock_cursor.execute.assert_any_call(
        "SELECT answersId FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify the INSERT query is executed
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (2, user_id, question_id)
    )


def test_upsert_single_answer_no_answer_found(mock_cursor):

    answer_value = "Nonexistent Answer"
    question_id = 103
    user_id = 7

    # Mock database responses
    # Simulate no answer found in the answers table
    mock_cursor.fetchone.side_effect = [None]

    # Call the function
    upsert_single_answer(mock_cursor, answer_value, question_id, user_id)

    # Verify SELECT query to find the answer ID
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, answer_value)
    )

    # Ensure no further queries are made since no answer was found
    assert mock_cursor.execute.call_count == 1


def test_upsert_single_answer_exception_handling(mock_cursor):

    answer_value = "Error Test Answer"
    question_id = 104
    user_id = 8

    # Mock the execute method to raise an exception
    mock_cursor.execute.side_effect = Exception("Database error")

    # Call the function and ensure no exception is produced
    try:
        upsert_single_answer(mock_cursor, answer_value, question_id, user_id)
    except Exception:
        pytest.fail("Exception was not handled in upsert_single_answer")

    # Verify the error was logged (can be checked by adding a log mock or print validation if necessary)
