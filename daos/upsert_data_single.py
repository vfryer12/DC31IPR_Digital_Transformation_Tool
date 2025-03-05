import logging

def upsert_single_answer(cursor, answer_value, question_id, user_id):
    try:
        logging.debug(f"Attempting to upsert answer: {answer_value} for Question ID: {question_id} and User ID: {user_id}")
        
        # Check if the answer already exists in the answers table
        query = "SELECT id FROM answers WHERE questionsId = %s AND answer = %s"
        cursor.execute(query, (question_id, answer_value))
        answer_record = cursor.fetchone()
        logging.debug(f"Answer record fetched: {answer_record}")

        if answer_record:
            answer_id = answer_record[0]
            logging.debug(f"Answer ID for Question {question_id}: {answer_id}")

            # Check if the user already has this specific answer for the question
            user_answer_query = "SELECT answersId FROM userAnswers WHERE userId = %s AND questionsId = %s"
            cursor.execute(user_answer_query, (user_id, question_id))
            user_answer_records = cursor.fetchall()
            logging.debug(f"User answer records fetched: {user_answer_records}")

            found_existing_answer = True if user_answer_records else False

            if found_existing_answer:
                update_sql = "UPDATE userAnswers SET answersId = %s WHERE userId = %s AND questionsId = %s"
                cursor.execute(update_sql, (answer_id, user_id, question_id))
                logging.debug(f"Updated answer for Question {question_id} and User {user_id}")
            else:
                # Insert the new data if no existing answer is found
                insert_sql = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"
                cursor.execute(insert_sql, (answer_id, user_id, question_id))
                logging.debug(f"Inserted new answer for Question {question_id} and User {user_id}")
        else:
            logging.debug(f"No answer found for question {question_id} and answer '{answer_value}'")
    except Exception as e:
        logging.debug(f"An error occurred: {e}")