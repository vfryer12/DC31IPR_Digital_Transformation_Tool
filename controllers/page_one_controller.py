import logging
from flask import Blueprint, render_template, request, redirect, url_for, session
from db_connector import create_connection, close_connection
from controllers.utils.mappings_page_one import answer_map_q1, answer_map_q2, answer_map_q3, answer_map_q4, answer_map_q5, answer_map_q6, answer_map_q7, answer_map_q8, answer_map_q9, answer_map_q10
from daos.upsert_data_single import upsert_single_answer
from daos.upsert_data_multiple import upsert_multiple_answers

page_one_bp = Blueprint('page_one', __name__)

@page_one_bp.route('/PageOneDigitalStrategy', methods=['GET', 'POST'])

def page_one_digital_strategy():
    logging.debug("page_one_digital_strategy inside function")
    logging.debug(request)
    if request.method == 'POST':
        logging.debug("POST page one request received")
        
        # Get form data
        question_one_values   = request.form.get('question-one')
        question_two_values   = request.form.get('question-two')
        question_three_values = request.form.get('question-three')
        question_four_values  = request.form.getlist('question-four')
        question_five_values  = request.form.getlist('question-five')
        question_six_values   = request.form.getlist('question-six')
        question_seven_values = request.form.getlist('question-seven')
        question_eight_values = request.form.getlist('question-eight')
        question_nine_values  = request.form.getlist('question-nine')
        question_ten_values   = request.form.getlist('question-ten')

        logging.debug(f"Received data - Question One: {question_one_values}, Question Two: {question_two_values}, Question Three: {question_three_values}, Question Four: {question_four_values}, Question Five: {question_five_values}, Question Six: {question_six_values}, Question Seven: {question_seven_values}, Question Eight: {question_eight_values}, Question Nine: {question_nine_values}, Question Ten: {question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            logging.debug(f"User ID from session: {user_id}")
        else:
            logging.debug("No user ID in session")
            return redirect(url_for('login.login'))

        # Ensure the form values are correctly mapped
        question_one_answer    = answer_map_q1.get(question_one_values, None)
        question_two_answer    = answer_map_q2.get(question_two_values, None)
        question_three_answer  = answer_map_q3.get(question_three_values, None)
        question_four_answers  = [answer_map_q4.get(value, None) for value in question_four_values]
        question_five_answers  = [answer_map_q5.get(value, None) for value in question_five_values]
        question_six_answers   = [answer_map_q6.get(value, None) for value in question_six_values]
        question_seven_answers = [answer_map_q7.get(value, None) for value in question_seven_values]
        question_eight_answers = [answer_map_q8.get(value, None) for value in question_eight_values]
        question_nine_answers  = [answer_map_q9.get(value, None) for value in question_nine_values]
        question_ten_answers   = [answer_map_q10.get(value, None) for value in question_ten_values]
        
        if not question_one_answer:
            logging.debug("Invalid answer for question one")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_two_answer:
            logging.debug("Invalid answer for question two")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_three_answer:
            logging.debug("Invalid answer for question three")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if len(question_four_answers) != 1 or None in question_four_answers:
            logging.debug("Invalid answer for question four: Must have exactly one valid answer")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if len(question_five_answers) > 3 or None in question_five_answers:
            logging.debug("Invalid answer for question five or more than three selections made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if len(question_six_answers) > 3 or None in question_six_answers:
            logging.debug("Invalid answer for question six or more than three selections made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if len(question_seven_answers) > 3 or None in question_seven_answers:
            logging.debug("Invalid answer for question seven or more than three selections made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if len(question_eight_answers) != 1 or None in question_eight_answers:
            logging.debug("Invalid answer for question eight or more than one selection made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if len(question_nine_answers) > 2 or None in question_nine_answers:
            logging.debug("Invalid answer for question nine or more than two selections made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if len(question_ten_answers) != 1 or None in question_ten_answers:
            logging.debug("Invalid answer for question te or more than one selection made")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        try:
            conn = create_connection()
            if conn:
                logging.debug("Connection established")
                cursor = conn.cursor()

                question_one_id   = 1
                question_two_id   = 2
                question_three_id = 3
                question_four_id  = 4
                question_five_id  = 5
                question_six_id   = 6
                question_seven_id = 7
                question_eight_id = 8
                question_nine_id  = 9
                question_ten_id   = 10

                # Single value handling
                upsert_single_answer(cursor, question_one_answer, question_one_id, user_id)
                upsert_single_answer(cursor, question_two_answer, question_two_id, user_id)
                upsert_single_answer(cursor, question_three_answer, question_three_id, user_id)

                # List value handling
                upsert_multiple_answers(cursor, question_four_answers, question_four_id, user_id)
                upsert_multiple_answers(cursor, question_five_answers, question_five_id, user_id)
                upsert_multiple_answers(cursor, question_six_answers, question_six_id, user_id)
                upsert_multiple_answers(cursor, question_seven_answers, question_seven_id, user_id)
                upsert_multiple_answers(cursor, question_eight_answers, question_eight_id, user_id)
                upsert_multiple_answers(cursor, question_nine_answers, question_nine_id, user_id)
                upsert_multiple_answers(cursor, question_ten_answers, question_ten_id, user_id)

                conn.commit()
                logging.debug("Successfully inserted/upserted data into userAnswers table")

                cursor.close()
            else:
                logging.debug("Failed to establish database connection")
                return redirect(url_for('page_one.page_one_digital_strategy'))

        except Exception as e:
            logging.debug(f"An error occurred: {e}")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_one.page_one_digital_strategy'))

    logging.debug("GET page one request received - Rendering form")
    return render_template('PageOneDigitalStrategy.html')