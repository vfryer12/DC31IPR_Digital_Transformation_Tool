from textwrap import dedent
from daos import mysql_queries

def get_section_answer_weights(conn, user_id:int) -> list[tuple[str,int,int]]:
    """
    Retrieves the user answers and associated weights from the database.
    (sectionname
	,answersid
	,weighting)
    """
    # try:
    cursor = conn.cursor()
    query = dedent(mysql_queries.USER_ANSWER_WEIGHTS)
    vals = run_sql(cursor, query, [user_id])
    cursor.close()
    return vals
    #     cursor.execute(query, (user_id,))
    #     weights = cursor.fetchall() # [(1,2)]
    #     return weights
    # except Exception as e:
    #     print(f"Error in get_user_weights: {e}")
    #     return None


def run_sql(cursor, query:str, params:list):
    try:
        cursor.execute(query, params)
        weights = cursor.fetchall() # [(1,2)]
        return weights
    except Exception as e:
        print(f"Error in query: {e}")
        return None