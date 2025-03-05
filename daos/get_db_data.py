import logging
from textwrap import dedent
from daos import mysql_queries
from collections import namedtuple

def get_section_answer_weights(conn, user_id: int) -> list[tuple[str, int, int]]:

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
            logging.debug(f"No solutions found for user_id {user_id}")
        return vals
    except Exception as e:
        logging.debug(f"Error retrieving solutions for user {user_id}: {e}")
        return []

def run_sql(cursor, query: str, params: list):

    try:
        # Execute the query with the provided parameters
        cursor.execute(query, params)

        DbRow = namedtuple("DbRow", [i.lower() for i in cursor.column_names])

        # Fetch all results from the executed query
        data = [DbRow(*row) for row in cursor.fetchall()]
        
        return data
    except Exception as e:
        # Debug the error message if there's an exception
        logging.debug(f"Error in query: {e}")
        
        return None