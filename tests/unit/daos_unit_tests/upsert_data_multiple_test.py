import pytest
from unittest.mock import MagicMock
from daos.upsert_data_multiple import upsert_multiple_answers


@pytest.fixture
def mock_cursor():
    """Fixture to create a mock cursor."""
    return MagicMock()


def test_upsert_multiple_answers_success(mock_cursor):
    # Example data
    answers_list = ["Answer 1", "Answer 2", "Answer 3"]
    question_id = 101
    user_id = 5

    # Mock database responses
    # Simulate finding the answer IDs for "Answer 1", "Answer 2", "Answer 3"
    mock_cursor.fetchone.side_effect = [
        (1,),  # Answer ID for "Answer 1"
        (2,),  # Answer ID for "Answer 2"
        (3,)   # Answer ID for "Answer 3"
    ]

    # Call the function
    upsert_multiple_answers(mock_cursor, answers_list, question_id, user_id)

    # Verify delete query is called once
    mock_cursor.execute.assert_any_call(
        "DELETE FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify the SELECT query is called for each answer
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Answer 1")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Answer 2")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Answer 3")
    )

    # Verify the INSERT query is called for each answer
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (1, user_id, question_id)
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (2, user_id, question_id)
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (3, user_id, question_id)
    )

    # Check the total number of `execute` calls
    assert mock_cursor.execute.call_count == 7  # 1 delete + 3 select + 3 insert


def test_upsert_multiple_answers_skip_missing(mock_cursor):
    # Example data with one missing answer
    answers_list = ["Answer 1", "Answer 2", "Missing Answer"]
    question_id = 102
    user_id = 6

    # Mock database responses
    mock_cursor.fetchone.side_effect = [
        (1,),  # Answer ID for "Answer 1"
        (2,),  # Answer ID for "Answer 2"
        None   # "Missing Answer" not found
    ]

    # Call the function
    upsert_multiple_answers(mock_cursor, answers_list, question_id, user_id)

    # Verify delete query is called
    mock_cursor.execute.assert_any_call(
        "DELETE FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify the SELECT query is called for each answer
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Answer 1")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Answer 2")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s",
        (question_id, "Missing Answer")
    )

    # Verify the INSERT query is called only for found answers
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (1, user_id, question_id)
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
        (2, user_id, question_id)
    )

    # Ensure no INSERT is called for "Missing Answer"
    for call in mock_cursor.execute.call_args_list:
        assert call[0][0] != (
            "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)",
            (None, user_id, question_id)
        )

    # Check the total number of `execute` calls
    assert mock_cursor.execute.call_count == 6  # 1 delete + 3 select + 2 insert