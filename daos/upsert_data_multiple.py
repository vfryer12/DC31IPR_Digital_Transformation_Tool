import logging

def upsert_multiple_answers(cursor, answers_list, question_id, user_id):

    try:
        logging.debug(f"Upserting answers: {answers_list} for Question ID: {question_id} and User ID: {user_id}")
        
        # Delete existing answers for the user and question
        delete_query = "DELETE FROM userAnswers WHERE userId = %s AND questionsId = %s"
        cursor.execute(delete_query, (user_id, question_id))
        logging.debug(f"Deleted existing answers for Question ID: {question_id} and User ID: {user_id}")
        
        # Loop through each answer and insert it
        for answer_value in answers_list:
            # Ensure the answer exists in the answers table and get its ID
            select_query = "SELECT id FROM answers WHERE questionsId = %s AND answer = %s"
            logging.debug(f"Executing SELECT query: {select_query} with {question_id}, {answer_value}")
            cursor.execute(select_query, (question_id, answer_value))
            answer_record = cursor.fetchone()

            if answer_record:
                answer_id = answer_record[0]
                
                # Fetch all remaining results (safeguard against unread results)
                cursor.fetchall() 

                # Insert the new answer into userAnswers
                insert_query = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"
                logging.debug(f"Executing INSERT query: {insert_query} with {answer_id}, {user_id}, {question_id}")
                cursor.execute(insert_query, (answer_id, user_id, question_id))
                logging.debug(f"Inserted answer '{answer_value}' for Question ID: {question_id} and User ID: {user_id}")
            else:
                logging.debug(f"Answer '{answer_value}' not found for Question ID: {question_id}. Skipping.")
    except Exception as e:
        logging.debug(f"An error occurred: {e}")