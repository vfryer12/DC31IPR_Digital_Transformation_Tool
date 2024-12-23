# get_db_data.py

from textwrap import dedent
from daos import mysql_queries

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

        # Fetch all results from the executed query
        weights = cursor.fetchall() # [(1,2)]
        
        return weights
    except Exception as e:
        # Print the error message if there's an exception
        print(f"Error in query: {e}")
        
        return None