def find_user_by_username(cursor, username):
    """
    Fetches a user record by username.

    Args:
        cursor: Database cursor object.
        username: The username to search for.

    Returns:
        A user record or None if the user is not found.
    """
    try:
        query = "SELECT * FROM user WHERE username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone()
    except Exception as e:
        print(f"Error in find_user_by_username: {e}")
        return None