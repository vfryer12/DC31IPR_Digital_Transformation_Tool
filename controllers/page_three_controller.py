import logging
from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.utils.mappings_page_three import answer_map_page_three_q1, answer_map_page_three_q2, answer_map_page_three_q3, answer_map_page_three_q4, answer_map_page_three_q5, answer_map_page_three_q6, answer_map_page_three_q7, answer_map_page_three_q8, answer_map_page_three_q9, answer_map_page_three_q10
from db_connector import create_connection, close_connection
from daos.upsert_data_multiple import upsert_multiple_answers

page_three_bp = Blueprint('page_three', __name__)

@page_three_bp.route('/PageThreeTechnologyAdoption', methods=['GET', 'POST'])

def page_three_technology_adoption():
    logging.debug("page_three_technology_adoption inside function")
    logging.debug(request)
    if request.method == 'POST':
        logging.debug('POST page three request received')

        # Get form data
        page_three_question_one_values   = request.form.getlist('page-three-question-one')
        page_three_question_two_values   = request.form.getlist('page-three-question-two')
        page_three_question_three_values = request.form.getlist('page-three-question-three')
        page_three_question_four_values  = request.form.getlist('page-three-question-four')
        page_three_question_five_values  = request.form.getlist('page-three-question-five')
        page_three_question_six_values   = request.form.getlist('page-three-question-six')
        page_three_question_seven_values = request.form.getlist('page-three-question-seven')
        page_three_question_eight_values = request.form.getlist('page-three-question-eight')
        page_three_question_nine_values  = request.form.getlist('page-three-question-nine')
        page_three_question_ten_values   = request.form.getlist('page-three-question-ten')

        logging.debug(f"Received data - Question One: {page_three_question_one_values}, Question Two: {page_three_question_two_values}, Question Three: {page_three_question_three_values}, Question Four: {page_three_question_four_values}, Question Five: {page_three_question_five_values}, Question Six: {page_three_question_six_values}, Question Seven: {page_three_question_seven_values}, Question Eight: {page_three_question_eight_values}, Question Nine: {page_three_question_nine_values}, Question Ten: {page_three_question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            logging.debug(f"User ID from session: {user_id}")
        else:
            logging.debug("No user ID in session")
            return redirect(url_for('login.login'))
        
        # Ensure the form values are correctly mapped
        page_three_question_one_answers   = [answer_map_page_three_q1.get(value, None) for value in page_three_question_one_values]
        page_three_question_two_answers   = [answer_map_page_three_q2.get(value, None) for value in page_three_question_two_values]
        page_three_question_three_answers = [answer_map_page_three_q3.get(value, None) for value in page_three_question_three_values]
        page_three_question_four_answers  = [answer_map_page_three_q4.get(value, None) for value in page_three_question_four_values]
        page_three_question_five_answers  = [answer_map_page_three_q5.get(value, None) for value in page_three_question_five_values]
        page_three_question_six_answers   = [answer_map_page_three_q6.get(value, None) for value in page_three_question_six_values]
        page_three_question_seven_answers = [answer_map_page_three_q7.get(value, None) for value in page_three_question_seven_values]
        page_three_question_eight_answers = [answer_map_page_three_q8.get(value, None) for value in page_three_question_eight_values]
        page_three_question_nine_answers  = [answer_map_page_three_q9.get(value, None) for value in page_three_question_nine_values]
        page_three_question_ten_answers   = [answer_map_page_three_q10.get(value, None) for value in page_three_question_ten_values]
        
                # Temporary separate mappings for easier debugging
        if len(page_three_question_one_answers) > 3 or None in page_three_question_one_answers:
            logging.debug("Invalid answer for page three, question one or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_two_answers) != 1 or None in page_three_question_two_answers:
            logging.debug("Invalid answer for page three, question two or more than 1 selection made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_three_answers) > 3 or None in page_three_question_three_answers:
            logging.debug("Invalid answer for page three, question three or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))

        if len(page_three_question_four_answers) > 3 or None in page_three_question_four_answers:
            logging.debug("Invalid answer for page three, question four or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_five_answers) > 3 or None in page_three_question_five_answers:
            logging.debug("Invalid answer for page three, question five or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_six_answers) > 3 or None in page_three_question_six_answers:
            logging.debug("Invalid answer for page three, question six or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_seven_answers) > 3 or None in page_three_question_seven_answers:
            logging.debug("Invalid answer for page three, question seven or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_eight_answers) > 3 or None in page_three_question_eight_answers:
            logging.debug("Invalid answer for page three, question eight or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_nine_answers) > 3 or None in page_three_question_nine_answers:
            logging.debug("Invalid answer for page three, question nine or more than 3 selections made")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        if len(page_three_question_ten_answers) > 3 or None in page_three_question_ten_answers:
            logging.debug("Invalid answer for page three, question ten")
            return redirect(url_for('page_three.page_three_technology_adoption'))
        
        try:
            conn = create_connection()
            if conn:
                logging.debug("Connection established")
                cursor = conn.cursor()

                question_one_id = 21
                question_two_id = 22 
                question_three_id = 23
                question_four_id = 24
                question_five_id = 25
                question_six_id = 26
                question_seven_id = 27
                question_eight_id = 28
                question_nine_id = 29
                question_ten_id = 30
                
                # List value handling
                upsert_multiple_answers(cursor, page_three_question_one_answers, question_one_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_two_answers, question_two_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_three_answers, question_three_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_four_answers, question_four_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_five_answers, question_five_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_six_answers, question_six_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_seven_answers, question_seven_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_eight_answers, question_eight_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_nine_answers, question_nine_id, user_id)
                upsert_multiple_answers(cursor, page_three_question_ten_answers, question_ten_id, user_id)

                conn.commit()
                logging.debug("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                logging.debug("Failed to establish database connection")
                return redirect(url_for('page_three.page_three_technology_adoption'))

        except Exception as e:
            logging.debug(f"An error occurred: {e}")
            return redirect(url_for('page_three.page_three_technology_adoption'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_three.page_three_technology_adoption'))

    logging.debug("GET Page three request received - Rendering form")
    return render_template('PageThreeTechnologyAdoption.html')
        