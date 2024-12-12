def authenticate_user(cursor, username, password):
    """
    Authenticates a user by username and password.

    Args:
        cursor: Database cursor object.
        username: The username to authenticate.
        password: The password to validate.

    Returns:
        A user record or None if authentication fails.
    """
    try:
        query = """
            SELECT * FROM user
            WHERE username = %s AND AES_DECRYPT(userpassword, 'encryption_key') = %s
        """
        cursor.execute(query, (username, password))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error in authenticate_user: {e}")
        return None
