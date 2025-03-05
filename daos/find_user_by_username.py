import logging

def find_user_by_username(cursor, username):
    try:
        query = "SELECT * FROM user WHERE username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone()
    except Exception as e:
        logging.debug(f"Error in find_user_by_username: {e}")
        return None