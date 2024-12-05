from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.utils.mappings_page_five import answer_map_page_five_q1, answer_map_page_five_q2, answer_map_page_five_q3, answer_map_page_five_q4, answer_map_page_five_q5, answer_map_page_five_q6, answer_map_page_five_q7, answer_map_page_five_q8, answer_map_page_five_q9, answer_map_page_five_q10
from db_connection import create_connection, close_connection
from daos.upsert_data_multiple import upsert_multiple_answers

page_five_bp = Blueprint('page_five', __name__)

@page_five_bp.route('/PageFiveDigitalMarketing', methods=['GET', 'POST'])

def page_five_digital_marketing():
    print("page_five_digital_marketing inside function")
    print(request)
    if request.method == 'POST':
        print('POST page five request received')

        # Get form data
        page_five_question_one_values   = request.form.getlist('page-five-question-one')
        page_five_question_two_values   = request.form.getlist('page-five-question-two')
        page_five_question_three_values = request.form.getlist('page-five-question-three')
        page_five_question_four_values  = request.form.getlist('page-five-question-four')
        page_five_question_five_values  = request.form.getlist('page-five-question-five')
        page_five_question_six_values   = request.form.getlist('page-five-question-six')
        page_five_question_seven_values = request.form.getlist('page-five-question-seven')
        page_five_question_eight_values = request.form.getlist('page-five-question-eight')
        page_five_question_nine_values  = request.form.getlist('page-five-question-nine')
        page_five_question_ten_values   = request.form.getlist('page-five-question-ten')

        print(f"Received data - Question One: {page_five_question_one_values}, Question Two: {page_five_question_two_values}, Question Three: {page_five_question_three_values}, Question Four: {page_five_question_four_values}, Question Five: {page_five_question_five_values}, Question Six: {page_five_question_six_values}, Question Seven: {page_five_question_seven_values}, Question Eight: {page_five_question_eight_values}, Question Nine: {page_five_question_nine_values}, Question Ten: {page_five_question_ten_values}")
        
        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
            return redirect(url_for('login.login'))
        
        # Ensure the form values are correctly mapped
        page_five_question_one_answers   = [answer_map_page_five_q1.get(value, None) for value in page_five_question_one_values]
        page_five_question_two_answers   = [answer_map_page_five_q2.get(value, None) for value in page_five_question_two_values]
        page_five_question_three_answers = [answer_map_page_five_q3.get(value, None) for value in page_five_question_three_values]
        page_five_question_four_answers  = [answer_map_page_five_q4.get(value, None) for value in page_five_question_four_values]
        page_five_question_five_answers  = [answer_map_page_five_q5.get(value, None) for value in page_five_question_five_values]
        page_five_question_six_answers   = [answer_map_page_five_q6.get(value, None) for value in page_five_question_six_values]
        page_five_question_seven_answers = [answer_map_page_five_q7.get(value, None) for value in page_five_question_seven_values]
        page_five_question_eight_answers = [answer_map_page_five_q8.get(value, None) for value in page_five_question_eight_values]
        page_five_question_nine_answers  = [answer_map_page_five_q9.get(value, None) for value in page_five_question_nine_values]
        page_five_question_ten_answers   = [answer_map_page_five_q10.get(value, None) for value in page_five_question_ten_values]
        
                # Has to be separate mappings ready for the validation checks

        if None in page_five_question_one_answers:
            print("Invalid answer for page five, question one")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_two_answers:
            print("Invalid answer for page five, question two")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_three_answers:
            print("Invalid answer for page five, question three")
            return redirect(url_for('page_five.page_five_digital_marketing'))

        if None in page_five_question_four_answers:
            print("Invalid answer for page five, question four")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_five_answers:
            print("Invalid answer for page five, question five")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_six_answers:
            print("Invalid answer for page five, question six")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_seven_answers:
            print("Invalid answer for page five, question seven")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_eight_answers:
            print("Invalid answer for page five, question eight")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_nine_answers:
            print("Invalid answer for page five, question nine")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        if None in page_five_question_ten_answers:
            print("Invalid answer for page five, question ten")
            return redirect(url_for('page_five.page_five_digital_marketing'))
        
        try:
            conn = create_connection()
            if conn:
                print("Connection established")
                cursor = conn.cursor()

                question_one_id   = 41
                question_two_id   = 42 
                question_three_id = 43
                question_four_id  = 44
                question_five_id  = 45
                question_six_id   = 46
                question_seven_id = 47
                question_eight_id = 48
                question_nine_id  = 49
                question_ten_id   = 50

                # List value handling
                upsert_multiple_answers(cursor, page_five_question_one_answers, question_one_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_two_answers, question_two_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_three_answers, question_three_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_four_answers, question_four_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_five_answers, question_five_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_six_answers, question_six_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_seven_answers, question_seven_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_eight_answers, question_eight_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_nine_answers, question_nine_id, user_id)
                upsert_multiple_answers(cursor, page_five_question_ten_answers, question_ten_id, user_id)

                conn.commit()
                print("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                print("Failed to establish database connection")
                return redirect(url_for('page_five.page_five_digital_marketing'))

        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect(url_for('page_five.page_five_digital_marketing'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_five.page_five_digital_marketing'))

    print("GET Page five request received - Rendering form")
    return render_template('PageFiveDigitalMarketing.html')
