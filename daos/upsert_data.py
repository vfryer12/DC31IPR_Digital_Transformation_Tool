def upsert_single_answer(cursor, answer_value, question_id, user_id):
    # Check if the answer already exists in the answers table
    query = "SELECT id FROM answers WHERE questionsId = %s AND answer = %s"
    cursor.execute(query, (question_id, answer_value))
    answer_record = cursor.fetchone()

    if answer_record:
        answer_id = answer_record[0]
        print(f"Answer ID for Question {question_id}: {answer_id}")

        # Check if the user already has an answer for the question
        user_answer_query = "SELECT id FROM userAnswers WHERE answersId = %s AND userId = %s AND questionsId = %s"
        cursor.execute(user_answer_query, (user_id, question_id))
        user_answer_record = cursor.fetchone()

        if user_answer_record:
            # If an answer already exists, update it instead of deleting
            update_sql = "UPDATE userAnswers SET answersId = %s WHERE id = %s"
            cursor.execute(update_sql, (answer_id, user_answer_record[0]))
            print(f"Updated answer for Question {question_id} and User {user_id}")
        else:
            # Insert the new data if no existing answer is found
            insert_sql = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"
            cursor.execute(insert_sql, (answer_id, user_id, question_id))
            print(f"Inserted new answer for Question {question_id}")
    else:
        print(f"No answer found for question {question_id} and answer '{answer_value}'")

def upsert_multiple_answers(cursor, answers_list, question_id, user_id):
    for answer in answers_list:
        upsert_single_answer(cursor, answer, question_id, user_id)
