# get_db_data.py

from unittest.mock import Mock
from daos import mysql_queries
from daos.get_db_data import get_section_answer_weights
from textwrap import dedent


def test_get_section_answer_weights_success():
    # Mock the database connection and cursor
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_conn.cursor.return_value = mock_cursor

    # Mock the cursor methods
    mock_cursor.column_names = ["section", "answersid", "weighting"]
    mock_cursor.fetchall.return_value = [("Section1", 1, 10), ("Section2", 2, 20)]

    # Call the function with the mock connection and a test user_id
    user_id = 123
    result = get_section_answer_weights(mock_conn, user_id)

    # Verify the results are as expected
    assert result == [("Section1", 1, 10), ("Section2", 2, 20)]
    mock_cursor.execute.assert_called_once_with(
        dedent(mysql_queries.USER_ANSWER_WEIGHTS), [user_id]
    )
    mock_cursor.close.assert_called_once()

def test_get_section_answer_weights_failure():
    # Mock the database connection and cursor
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_conn.cursor.return_value = mock_cursor

    # Simulate an exception during SQL execution
    mock_cursor.execute.side_effect = Exception("Database error")

    # Call the function with the mock connection and a test user_id
    user_id = 123
    result = get_section_answer_weights(mock_conn, user_id)

    # Verify that the result is None on failure
    assert result is None
    # Ensure the cursor was created
    mock_conn.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(
        """WITH sectquest
AS (
	SELECT s.section
		,q.id AS questionsId
	FROM sections AS s
	INNER JOIN questions AS q ON q.sectionid = s.id
	)
	,useransweight
AS (
	SELECT ua.answersId
		,a.weighting
		,a.questionsId
	FROM useranswers AS ua
	INNER JOIN answers AS a ON ua.answersId = a.id
	WHERE ua.userid = %s
	)
	,section_answer_weight
AS (
	SELECT sq.section
		,uw.answersid
		,uw.weighting
	FROM useransweight AS uw
	INNER JOIN sectquest AS sq ON uw.questionsId = sq.questionsId
	)
SELECT section
	,answersid
	,weighting
FROM section_answer_weight
""",
        [user_id],
    )

    mock_cursor.close.assert_called_once()