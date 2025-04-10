import logging
from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.utils.mappings_page_four import answer_map_page_four_q1, answer_map_page_four_q2, answer_map_page_four_q3, answer_map_page_four_q4, answer_map_page_four_q5, answer_map_page_four_q6, answer_map_page_four_q7, answer_map_page_four_q8, answer_map_page_four_q9, answer_map_page_four_q10
from db_connector import create_connection, close_connection
from daos.upsert_data_multiple import upsert_multiple_answers

page_four_bp = Blueprint('page_four', __name__)

@page_four_bp.route('/PageFourMarketTrends', methods=['GET', 'POST'])

def page_four_market_trends():
    logging.debug("page_four_market_trends inside function")
    logging.debug(request)
    if request.method == 'POST':
        logging.debug('POST page four request received')

        # Get form data
        page_four_question_one_values   = request.form.getlist('page-four-question-one')
        page_four_question_two_values   = request.form.getlist('page-four-question-two')
        page_four_question_three_values = request.form.getlist('page-four-question-three')
        page_four_question_four_values  = request.form.getlist('page-four-question-four')
        page_four_question_five_values  = request.form.getlist('page-four-question-five')
        page_four_question_six_values   = request.form.getlist('page-four-question-six')
        page_four_question_seven_values = request.form.getlist('page-four-question-seven')
        page_four_question_eight_values = request.form.getlist('page-four-question-eight')
        page_four_question_nine_values  = request.form.getlist('page-four-question-nine')
        page_four_question_ten_values   = request.form.getlist('page-four-question-ten')

        logging.debug(f"Received data - Question One: {page_four_question_one_values}, Question Two: {page_four_question_two_values}, Question Three: {page_four_question_three_values}, Question Four: {page_four_question_four_values}, Question Five: {page_four_question_five_values}, Question Six: {page_four_question_six_values}, Question Seven: {page_four_question_seven_values}, Question Eight: {page_four_question_eight_values}, Question Nine: {page_four_question_nine_values}, Question Ten: {page_four_question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            logging.debug(f"User ID from session: {user_id}")
        else:
            logging.debug("No user ID in session")
            return redirect(url_for('login.login'))
        
        # Ensure the form values are correctly mapped
        page_four_question_one_answers   = [answer_map_page_four_q1.get(value, None) for value in page_four_question_one_values]
        page_four_question_two_answers   = [answer_map_page_four_q2.get(value, None) for value in page_four_question_two_values]
        page_four_question_three_answers = [answer_map_page_four_q3.get(value, None) for value in page_four_question_three_values]
        page_four_question_four_answers  = [answer_map_page_four_q4.get(value, None) for value in page_four_question_four_values]
        page_four_question_five_answers  = [answer_map_page_four_q5.get(value, None) for value in page_four_question_five_values]
        page_four_question_six_answers   = [answer_map_page_four_q6.get(value, None) for value in page_four_question_six_values]
        page_four_question_seven_answers = [answer_map_page_four_q7.get(value, None) for value in page_four_question_seven_values]
        page_four_question_eight_answers = [answer_map_page_four_q8.get(value, None) for value in page_four_question_eight_values]
        page_four_question_nine_answers  = [answer_map_page_four_q9.get(value, None) for value in page_four_question_nine_values]
        page_four_question_ten_answers   = [answer_map_page_four_q10.get(value, None) for value in page_four_question_ten_values]
        
        # Temporary separate mappings for easier debugging

        if len(page_four_question_one_answers) > 3 or None in page_four_question_one_answers:
            logging.debug("Invalid answer for page four, question one or more than 3 selections made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_two_answers) != 1 or None in page_four_question_two_answers:
            logging.debug("Invalid answer for page four, question two or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_three_answers) > 3 or None in page_four_question_three_answers:
            logging.debug("Invalid answer for page four, question three or more than 3 selections made")
            return redirect(url_for('page_four.page_four_market_trends'))

        if len(page_four_question_four_answers) != 1 or None in page_four_question_four_answers:
            logging.debug("Invalid answer for page four, question four or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_five_answers) != 1 or None in page_four_question_five_answers:
            logging.debug("Invalid answer for page four, question five or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_six_answers) > 3 or None in page_four_question_six_answers:
            logging.debug("Invalid answer for page four, question six or more than 3 selections made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_seven_answers) > 3 or None in page_four_question_seven_answers:
            logging.debug("Invalid answer for page four, question seven or more than 3 selections made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_eight_answers) != 1 or None in page_four_question_eight_answers:
            logging.debug("Invalid answer for page four, question eight or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_nine_answers) != 1 or None in page_four_question_nine_answers:
            logging.debug("Invalid answer for page four, question nine or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if len(page_four_question_ten_answers) != 1  or None in page_four_question_ten_answers:
            logging.debug("Invalid answer for page four, question ten or more than 1 selection made")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        try:
            conn = create_connection()
            if conn:
                logging.debug("Connection established")
                cursor = conn.cursor()

                question_one_id   = 31
                question_two_id   = 32 
                question_three_id = 33
                question_four_id  = 34
                question_five_id  = 35
                question_six_id   = 36
                question_seven_id = 37
                question_eight_id = 38
                question_nine_id  = 39
                question_ten_id   = 40

                # List value handling
                upsert_multiple_answers(cursor, page_four_question_one_answers, question_one_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_two_answers, question_two_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_three_answers, question_three_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_four_answers, question_four_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_five_answers, question_five_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_six_answers, question_six_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_seven_answers, question_seven_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_eight_answers, question_eight_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_nine_answers, question_nine_id, user_id)
                upsert_multiple_answers(cursor, page_four_question_ten_answers, question_ten_id, user_id)

                conn.commit()
                logging.debug("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                logging.debug("Failed to establish database connection")
                return redirect(url_for('page_four.page_four_market_trends'))

        except Exception as e:
            logging.debug(f"An error occurred: {e}")
            return redirect(url_for('page_four.page_four_market_trends'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_four.page_four_market_trends'))

    logging.debug("GET Page four request received - Rendering form")
    return render_template('PageFourMarketTrends.html')
