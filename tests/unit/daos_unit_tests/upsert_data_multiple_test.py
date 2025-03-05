import pytest
from unittest.mock import MagicMock, call
from daos.upsert_data_multiple import upsert_multiple_answers


@pytest.fixture
def mock_cursor():

    return MagicMock()

def test_upsert_multiple_answers_success(mock_cursor):
    answers_list = ["Answer 1", "Answer 2", "Answer 3"]
    question_id = 101
    user_id = 5

    # Mock database responses
    mock_cursor.fetchone.side_effect = [
        (1,),  # ID for "Answer 1"
        (2,),  # ID for "Answer 2"
        (3,)   # ID for "Answer 3"
    ]

    upsert_multiple_answers(mock_cursor, answers_list, question_id, user_id)

    # Verify the delete query
    mock_cursor.execute.assert_any_call(
        "DELETE FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify SELECT queries
    select_calls = [
        call("SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Answer 1")),
        call("SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Answer 2")),
        call("SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Answer 3"))
    ]
    mock_cursor.execute.assert_has_calls(select_calls, any_order=True)

    # Verify INSERT queries
    insert_calls = [
        call("INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)", (1, user_id, question_id)),
        call("INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)", (2, user_id, question_id)),
        call("INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)", (3, user_id, question_id))
    ]
    mock_cursor.execute.assert_has_calls(insert_calls, any_order=True)

    # Assert the total number of queries executed
    # 1 DELETE + 3 SELECT + 3 INSERT
    assert mock_cursor.execute.call_count == 7


def test_upsert_multiple_answers_skip_missing(mock_cursor):
    answers_list = ["Answer 1", "Answer 2", "Missing Answer"]
    question_id = 102
    user_id = 6

    # Mock database responses
    mock_cursor.fetchone.side_effect = [
        (1,),  # ID for "Answer 1"
        (2,),  # ID for "Answer 2"
        None   # No ID for "Missing Answer"
    ]

    upsert_multiple_answers(mock_cursor, answers_list, question_id, user_id)

    # Verify the delete query
    mock_cursor.execute.assert_any_call(
        "DELETE FROM userAnswers WHERE userId = %s AND questionsId = %s",
        (user_id, question_id)
    )

    # Verify SELECT queries
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Answer 1")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Answer 2")
    )
    mock_cursor.execute.assert_any_call(
        "SELECT id FROM answers WHERE questionsId = %s AND answer = %s", (question_id, "Missing Answer")
    )

    # Verify INSERT queries only for found answers
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)", (1, user_id, question_id)
    )
    mock_cursor.execute.assert_any_call(
        "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)", (2, user_id, question_id)
    )

    # Ensure no INSERT for "Missing Answer"
    assert not any(
        call[0][0] == "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)" and
        call[0][1][0] is None
        for call in mock_cursor.execute.call_args_list
    )

    # Assert the total number of queries executed
    # 1 DELETE + 3 SELECT + 2 INSERT
    assert mock_cursor.execute.call_count == 6