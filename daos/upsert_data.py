def upsert_single_answer(cursor, answer_value, question_id, user_id, sql):
    query = "SELECT id FROM answers WHERE questionsId = %s AND answer = %s"
    cursor.execute(query, (question_id, answer_value))
    answer_record = cursor.fetchone()
    if answer_record:
        answer_id = answer_record[0]
        print(f"Answer ID for Question {question_id}: {answer_id}")
        cursor.execute(sql, (answer_id, user_id, question_id))
    else:
        print(f"No answer found for question {question_id} and answer '{answer_value}'")

def upsert_multiple_answers(cursor, answers_list, question_id, user_id, sql):
    for answer in answers_list:
        upsert_single_answer(cursor, answer, question_id, user_id, sql)