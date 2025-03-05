import logging

def authenticate_user(cursor, username, password):

    try:
        query = """
            SELECT * FROM user
            WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s
        """
        cursor.execute(query, (username, password))
        return cursor.fetchone()
    except Exception as e:
        logging.debug(f"Error in authenticate_user: {e}")
        return None
