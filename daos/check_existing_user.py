def check_existing_user(cursor, username, email):
    query = "SELECT * FROM user WHERE username = %s OR useremail = %s"
    cursor.execute(query, (username, email))
    return cursor.fetchone()