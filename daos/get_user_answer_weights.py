def get_user_answer_weights(cursor, user_id):
    """
    Retrieves the user answers and associated weights from the database.

    Args:
        cursor: Database cursor object.
        user_id: The ID of the user whose weights need to be fetched.

    Returns:
        List of tuples containing question ID and the corresponding weighting, or None if an error occurs.
    """
    try:
        query = """
            SELECT ua.questionsId, a.weighting
            FROM userAnswers ua
            JOIN answers a ON ua.answersId = a.id
            WHERE ua.userId = %s
        """
        cursor.execute(query, (user_id,))
        weights = cursor.fetchall()

        return weights

    except Exception as e:
        print(f"Error in get_user_weights: {e}")
        return None
