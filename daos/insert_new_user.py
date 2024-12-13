def insert_new_user(cursor, username, password, email):
    """
    Inserts a new user into the database with an encrypted password.

    Args:
        cursor: Database cursor object.
        username: The username of the new user.
        password: The plaintext password to be encrypted.
        email: The email of the new user.

    Returns:
        None
    """
    encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, {encrypted_password_query}, %s)
    """
    cursor.execute(query, (username, password, email))
