import logging
from flask import Blueprint, request, session, url_for, redirect, render_template
from db_connector import create_connection, close_connection
from controllers.utils.mappings_page_two import answer_map_page_two_q1, answer_map_page_two_q2, answer_map_page_two_q3, answer_map_page_two_q4, answer_map_page_two_q5, answer_map_page_two_q6, answer_map_page_two_q7, answer_map_page_two_q8, answer_map_page_two_q9, answer_map_page_two_q10
from daos.upsert_data_multiple import upsert_multiple_answers

page_two_bp = Blueprint('page_two', __name__)

@page_two_bp.route('/PageTwoDigitalSkills', methods=['GET', 'POST'])

def page_two_digital_skills():
    logging.debug("page_two_digital_skills inside function")
    logging.debug(request)
    if request.method == 'POST':
        logging.debug("POST page two request received")

        # Get form data
        page_two_question_one_values   = request.form.getlist('page-two-question-one')
        page_two_question_two_values   = request.form.getlist('page-two-question-two')
        page_two_question_three_values = request.form.getlist('page-two-question-three')
        page_two_question_four_values  = request.form.getlist('page-two-question-four')
        page_two_question_five_values  = request.form.getlist('page-two-question-five')
        page_two_question_six_values   = request.form.getlist('page-two-question-six')
        page_two_question_seven_values = request.form.getlist('page-two-question-seven')
        page_two_question_eight_values = request.form.getlist('page-two-question-eight')
        page_two_question_nine_values  = request.form.getlist('page-two-question-nine')
        page_two_question_ten_values   = request.form.getlist('page-two-question-ten')

        logging.debug(f"Received data - Question One: {page_two_question_one_values}, Question Two: {page_two_question_two_values}, Question Three: {page_two_question_three_values}, Question Four: {page_two_question_four_values}, Question Five: {page_two_question_five_values}, Question Six: {page_two_question_six_values}, Question Seven: {page_two_question_seven_values}, Question Eight: {page_two_question_eight_values}, Question Nine: {page_two_question_nine_values}, Question Ten: {page_two_question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            logging.debug(f"User ID from session: {user_id}")
        else:
            logging.debug("No user ID in session")
            return redirect(url_for('login.login'))
        
        # Ensure the form values are correctly mapped
        page_two_question_one_answers   = [answer_map_page_two_q1.get(value, None) for value in page_two_question_one_values]
        page_two_question_two_answers   = [answer_map_page_two_q2.get(value, None) for value in page_two_question_two_values]
        page_two_question_three_answers = [answer_map_page_two_q3.get(value, None) for value in page_two_question_three_values]
        page_two_question_four_answers  = [answer_map_page_two_q4.get(value, None) for value in page_two_question_four_values]
        page_two_question_five_answers  = [answer_map_page_two_q5.get(value, None) for value in page_two_question_five_values]
        page_two_question_six_answers   = [answer_map_page_two_q6.get(value, None) for value in page_two_question_six_values]
        page_two_question_seven_answers = [answer_map_page_two_q7.get(value, None) for value in page_two_question_seven_values]
        page_two_question_eight_answers = [answer_map_page_two_q8.get(value, None) for value in page_two_question_eight_values]
        page_two_question_nine_answers  = [answer_map_page_two_q9.get(value, None) for value in page_two_question_nine_values]
        page_two_question_ten_answers   = [answer_map_page_two_q10.get(value, None) for value in page_two_question_ten_values]
        
        # Temporary separate mappings for easier debugging

        if len(page_two_question_one_answers) > 3 or None in page_two_question_one_answers:
            logging.debug("Invalid answer for page two, question one or more than 3 selections made.")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_two_answers) > 3 or None in page_two_question_two_answers:
            logging.debug("Invalid answer for page two, question two or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_three_answers) > 3 or None in page_two_question_three_answers:
            logging.debug("Invalid answer for page two, question three or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))

        if len(page_two_question_four_answers) > 3 or None in page_two_question_four_answers:
            logging.debug("Invalid answer for page two, question four or mroe than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_five_answers) > 3 or None in page_two_question_five_answers:
            logging.debug("Invalid answer for page two, question five or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_six_answers) > 3 or None in page_two_question_six_answers:
            logging.debug("Invalid answer for page two, question six or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_seven_answers) > 3 or None in page_two_question_seven_answers:
            logging.debug("Invalid answer for page two, question seven or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))

        if len(page_two_question_eight_answers) > 3 or None in page_two_question_eight_answers:
            logging.debug("Invalid answer for page two, question eight or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_nine_answers) > 3 or None in page_two_question_nine_answers:
            logging.debug("Invalid answer for page two, question nine or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if len(page_two_question_ten_answers) > 3 or None in page_two_question_ten_answers:
            logging.debug("Invalid answer for page two, question ten or more than 3 selections made")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        try:
            conn = create_connection()
            if conn:
                logging.debug("Connection established")
                cursor = conn.cursor()

                question_one_id   = 11
                question_two_id   = 12 
                question_three_id = 13
                question_four_id  = 14
                question_five_id  = 15
                question_six_id   = 16
                question_seven_id = 17
                question_eight_id = 18
                question_nine_id  = 19
                question_ten_id   = 20

                # List value handling
                upsert_multiple_answers(cursor, page_two_question_one_answers, question_one_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_two_answers, question_two_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_three_answers, question_three_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_four_answers, question_four_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_five_answers, question_five_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_six_answers, question_six_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_seven_answers, question_seven_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_eight_answers, question_eight_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_nine_answers, question_nine_id, user_id)
                upsert_multiple_answers(cursor, page_two_question_ten_answers, question_ten_id, user_id)

                conn.commit()
                logging.debug("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                logging.debug("Failed to establish database connection")
                return redirect(url_for('page_two.page_two_digital_skills'))

        except Exception as e:
            logging.debug(f"An error occurred: {e}")
            return redirect(url_for('page_two.page_two_digital_skills'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_two.page_two_digital_skills'))

    logging.debug("GET page two request received - Rendering form")
    return render_template('PageTwoDigitalSkills.html')