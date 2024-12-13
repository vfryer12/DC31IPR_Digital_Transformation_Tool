def check_existing_user(cursor, username, email):
    """
    Checks if a user with the given username or email already exists.

    Args:
        cursor: Database cursor object.
        username: The username to check.
        email: The email to check.

    Returns:
        The user record if found, otherwise None.
    """
    query = "SELECT * FROM user WHERE username = %s OR useremail = %s"
    cursor.execute(query, (username, email))
    return cursor.fetchone()