# get_db_data.py

from textwrap import dedent
from daos import mysql_queries
from collections import namedtuple

def get_section_answer_weights(conn, user_id: int) -> list[tuple[str, int, int]]:
    """
    Retrieves the user's answers and associated weights from the database.

    Args:
        conn: The database connection object.
        user_id (int): The user's ID.

    Returns:
        list[tuple[str, int, int]]: A list of tuples containing section name, answer ID, and weighting.
    """
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Use dedent to format the query from the mysql_queries module
    query = dedent(mysql_queries.USER_ANSWER_WEIGHTS)

    # Execute the query with the provided user_id and get the results
    vals = run_sql(cursor, query, [user_id])

    # Close the cursor
    cursor.close()

    return vals

def get_answer_solutions(conn, user_id: int) -> list[tuple[int, int, int, str, int]]:
    """Returns (question, questionsId, answersId, weighting, solution, weight_row_rank)"""
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Format the query
        query = dedent(mysql_queries.GET_USER_SOLUTIONS)

        # Execute the query and fetch the results
        vals = run_sql(cursor, query, [user_id])

        # Close the cursor
        cursor.close()

        # Check if solutions were found
        if not vals:
            print(f"No solutions found for user_id {user_id}")
        return vals
    except Exception as e:
        print(f"Error retrieving solutions for user {user_id}: {e}")
        return []


def run_sql(cursor, query: str, params: list):
    """
    Executes a given SQL query with provided parameters.

    Args:
        cursor: The database cursor object.
        query (str): The SQL query to execute.
        params (list): The list of parameters to pass to the SQL query.

    Returns:
        list: The fetched results from the query execution.
    """
    try:
        # Execute the query with the provided parameters
        cursor.execute(query, params)

        DbRow = namedtuple("DbRow", [i.lower() for i in cursor.column_names])

        # Fetch all results from the executed query
        data = [DbRow(*row) for row in cursor.fetchall()]
        
        return data
    except Exception as e:
        # Print the error message if there's an exception
        print(f"Error in query: {e}")
        
        return None