from flask import Blueprint, request, session, url_for, redirect, render_template
from controllers.utils.mappings_page_two import answer_map_page_two_q1, answer_map_page_two_q2, answer_map_page_two_q3, answer_map_page_two_q4, answer_map_page_two_q5, answer_map_page_two_q6, answer_map_page_two_q7, answer_map_page_two_q8, answer_map_page_two_q9, answer_map_page_two_q10
from db_connection import create_connection, close_connection, sql

page_two_bp = Blueprint('page_two', __name__)

@page_two_bp.route('/PageTwoDigitalSkills', methods=['GET', 'POST'])

def page_two_digital_skills():
    print("page_two_digital_skills inside function")
    print(request)
    if request.method == 'POST':
        print("POST page two request received")

        # Get form data
        page_two_question_one_values   = request.form.get('page-two-question-one')
        page_two_question_two_values   = request.form.get('page-two-question-two')
        page_two_question_three_values = request.form.get('page-two-question-three')
        page_two_question_four_values  = request.form.getlist('page-two-question-four')
        page_two_question_five_values  = request.form.getlist('page-two-question-five')
        page_two_question_six_values   = request.form.getlist('page-two-question-six')
        page_two_question_seven_values = request.form.getlist('page-two-question-seven')
        page_two_question_eight_values = request.form.getlist('page-two-question-eight')
        page_two_question_nine_values  = request.form.getlist('page-two-question-nine')
        page_two_question_ten_values   = request.form.getlist('page-two-question-ten')

        print(f"Received data - Question One: {page_two_question_one_values}, Question Two: {page_two_question_two_values}, Question Three: {page_two_question_three_values}, Question Four: {page_two_question_four_values}, Question Five: {page_two_question_five_values}, Question Six: {page_two_question_six_values}, Question Seven: {page_two_question_seven_values}, Question Eight: {page_two_question_eight_values}, Question Nine: {page_two_question_nine_values}, Question Ten: {page_two_question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
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
        
        # Has to be separate mappings ready for the validation checks

        if None in page_two_question_one_answers:
            print("Invalid answer for page two, question one")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_two_answers:
            print("Invalid answer for page two, question two")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_three_answers:
            print("Invalid answer for page two, question three")
            return redirect(url_for('page_two.page_two_digital_skills'))

        if None in page_two_question_four_answers:
            print("Invalid answer for page two, question four")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_five_answers:
            print("Invalid answer for page two, question five")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_six_answers:
            print("Invalid answer for page two, question six")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_seven_answers:
            print("Invalid answer for page two, question seven")
            return redirect(url_for('page_two.page_two_digital_skills'))

        if None in page_two_question_eight_answers:
            print("Invalid answer for page two, question eight")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_nine_answers:
            print("Invalid answer for page two, question nine")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        if None in page_two_question_ten_answers:
            print("Invalid answer for page two, question ten")
            return redirect(url_for('page_two.page_two_digital_skills'))
        
        try:
            conn = create_connection()
            if conn:
                print("Connection established")
                cursor = conn.cursor()

                question_one_id = 11
                question_two_id = 12
                question_three_id = 13
                question_four_id = 14
                question_five_id = 15
                question_six_id = 16
                question_seven_id = 17
                question_eight_id = 18
                question_nine_id = 19
                question_ten_id = 20

                for answer in page_two_question_one_answers:
                    query_one = "SELECT id FROM answers WHERE questionsId = 11 AND answer = %s"
                    cursor.execute(query_one, (answer,))
                    answer_one = cursor.fetchone()
                    if answer_one:
                        answer_one_id = answer_one[0]
                        print(f"Page two, answer one ID: {answer_one_id}")
                        cursor.execute(sql, (answer_one_id, user_id, question_one_id))
                    else:
                        print("No answer found for page two, question one")
                        return redirect(url_for('page_two.page_two_digital_skills'))
                    
                for answer in page_two_question_two_answers:
                    query_two = "SELECT id FROM answers WHERE questionsId = 12 AND answer = %s"
                    cursor.execute(query_two, (answer,))
                    answer_two = cursor.fetchone()
                    if answer_two:
                        answer_two_id = answer_two[0]
                        print(f"Page two, answer two ID: {answer_two_id}")
                        cursor.execute(sql, (answer_two_id, user_id, question_two_id))
                    else:
                        print("No answer found for page two, question two")
                        return redirect(url_for('page_two.page_two_digital_skills'))
                    
                for answer in page_two_question_three_answers:
                    query_three = "SELECT id FROM answers WHERE questionsId = 13 AND answer = %s"
                    cursor.execute(query_three, (answer,))
                    answer_three = cursor.fetchone()
                    if answer_three:
                        answer_three_id = answer_three[0]
                        print(f"Page two, answer two ID: {answer_three_id}")
                        cursor.execute(sql, (answer_three_id, user_id, question_three_id))
                    else:
                        print("No answer found for page three, question two")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_four_answers:
                    query_four = "SELECT id FROM answers WHERE questionsId = 14 AND answer = %s"
                    cursor.execute(query_four, (answer,))
                    answer_four = cursor.fetchone()
                    if answer_four:
                        answer_four_id = answer_four[0]
                        print(f"Page two, answer four ID: {answer_four_id}")
                        cursor.execute(sql, (answer_four_id, user_id, question_four_id))
                    else:
                        print("No answer found for page two, question four")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_five_answers:
                    query_five = "SELECT id FROM answers WHERE questionsId = 15 AND answer = %s"
                    cursor.execute(query_five, (answer,))
                    answer_five = cursor.fetchone()
                    if answer_five:
                        answer_five_id = answer_five[0]
                        print(f"Page two, answer five ID: {answer_five_id}")
                        cursor.execute(sql, (answer_five_id, user_id, question_five_id))
                    else:
                        print("No answer found for page two, question five")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_six_answers:
                    query_six = "SELECT id FROM answers WHERE questionsId = 16 AND answer = %s"
                    cursor.execute(query_six, (answer,))
                    answer_six = cursor.fetchone()
                    if answer_six:
                        answer_six_id = answer_six[0]
                        print(f"Page two, answer six ID: {answer_six_id}")
                        cursor.execute(sql, (answer_six_id, user_id, question_six_id))
                    else:
                        print("No answer found for page two, question six")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_seven_answers:
                    query_seven = "SELECT id FROM answers WHERE questionsId = 17 AND answer = %s"
                    cursor.execute(query_seven, (answer,))
                    answer_seven = cursor.fetchone()
                    if answer_seven:
                        answer_seven_id = answer_seven[0]
                        print(f"Page two, answer seven ID: {answer_seven_id}")
                        cursor.execute(sql, (answer_seven_id, user_id, question_seven_id))
                    else:
                        print("No answer found for page two, question seven")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_eight_answers:
                    query_eight = "SELECT id FROM answers WHERE questionsId = 18 AND answer = %s"
                    cursor.execute(query_eight, (answer,))
                    answer_eight = cursor.fetchone()
                    if answer_eight:
                        answer_eight_id = answer_eight[0]
                        print(f"Page two, answer eight ID: {answer_eight_id}")
                        cursor.execute(sql, (answer_eight_id, user_id, question_eight_id))
                    else:
                        print("No answer found for page two, question eight")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_nine_answers:
                    query_nine = "SELECT id FROM answers WHERE questionsId = 19 AND answer = %s"
                    cursor.execute(query_nine, (answer,))
                    answer_nine = cursor.fetchone()
                    if answer_nine:
                        answer_nine_id = answer_nine[0]
                        print(f"Page two, answer nine ID: {answer_nine_id}")
                        cursor.execute(sql, (answer_nine_id, user_id, question_nine_id))
                    else:
                        print("No answer found for page two, question nine")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                for answer in page_two_question_ten_answers:
                    query_ten = "SELECT id FROM answers WHERE questionsId = 20 AND answer = %s"
                    cursor.execute(query_ten, (answer,))
                    answer_ten = cursor.fetchone()
                    if answer_ten:
                        answer_ten_id = answer_ten[0]
                        print(f"Page two, answer ten ID: {answer_ten_id}")
                        cursor.execute(sql, (answer_ten_id, user_id, question_ten_id))
                    else:
                        print("No answer found for page two, question ten")
                        return redirect(url_for('page_two.page_two_digital_skills'))

                conn.commit()
                print("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                print("Failed to establish database connection")
                return redirect(url_for('page_two.page_two_digital_skills'))

        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect(url_for('page_two.page_two_digital_skills'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_two.page_two_digital_skills'))

    print("GET page two request received - Rendering form")
    return render_template('PageTwoDigitalSkills.html')