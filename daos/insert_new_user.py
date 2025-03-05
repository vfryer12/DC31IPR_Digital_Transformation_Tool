def insert_new_user(cursor, username, password, email):
    
    encrypted_password_query = "AES_ENCRYPT(%s, 'encryption_key')"
    query = f"""
        INSERT INTO user (username, userpassword, useremail)
        VALUES (%s, {encrypted_password_query}, %s)
    """
    cursor.execute(query, (username, password, email))
