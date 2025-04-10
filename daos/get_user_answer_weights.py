import logging
from textwrap import dedent

def get_user_answer_weights(cursor, user_id:int) -> list[tuple[int,int]]:

    try:
        query = dedent("""
            SELECT ua.questionsId, a.weighting
            FROM userAnswers ua
            JOIN answers a ON ua.answersId = a.id
            WHERE ua.userId = %s
        """)
        cursor.execute(query, (user_id,))
        weights = cursor.fetchall() # [(1,2)]
        return weights
    except Exception as e:
        logging.debug(f"Error in get_user_weights: {e}")
        return None