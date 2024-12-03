from flask import Blueprint, request, session, redirect, url_for, render_template
from controllers.utils.mappings_page_four import answer_map_page_four_q1, answer_map_page_four_q2, answer_map_page_four_q3, answer_map_page_four_q4, answer_map_page_four_q5, answer_map_page_four_q6, answer_map_page_four_q7, answer_map_page_four_q8, answer_map_page_four_q9, answer_map_page_four_q10
from db_connection import create_connection, close_connection

page_four_bp = Blueprint('page_four', __name__)

@page_four_bp.route('/PageFourMarketTrends', methods=['GET', 'POST'])

def page_four_market_trends():
    print("page_four_market_trends inside function")
    print(request)
    if request.method == 'POST':
        print('POST page four request received')

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

        print(f"Received data - Question One: {page_four_question_one_values}, Question Two: {page_four_question_two_values}, Question Three: {page_four_question_three_values}, Question Four: {page_four_question_four_values}, Question Five: {page_four_question_five_values}, Question Six: {page_four_question_six_values}, Question Seven: {page_four_question_seven_values}, Question Eight: {page_four_question_eight_values}, Question Nine: {page_four_question_nine_values}, Question Ten: {page_four_question_ten_values}")

        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
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
        
        # Has to be separate mappings ready for the validation checks

        if None in page_four_question_one_answers:
            print("Invalid answer for page four, question one")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_two_answers:
            print("Invalid answer for page four, question two")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_three_answers:
            print("Invalid answer for page four, question three")
            return redirect(url_for('page_four.page_four_market_trends'))

        if None in page_four_question_four_answers:
            print("Invalid answer for page four, question four")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_five_answers:
            print("Invalid answer for page four, question five")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_six_answers:
            print("Invalid answer for page four, question six")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_seven_answers:
            print("Invalid answer for page four, question seven")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_eight_answers:
            print("Invalid answer for page four, question eight")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_nine_answers:
            print("Invalid answer for page four, question nine")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        if None in page_four_question_ten_answers:
            print("Invalid answer for page four, question ten")
            return redirect(url_for('page_four.page_four_market_trends'))
        
        try:
            conn = create_connection()
            if conn:
                print("Connection established")
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

                sql = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"

                for answer in page_four_question_one_answers:
                    query_one = "SELECT id FROM answers WHERE questionsId = 31 AND answer = %s"
                    cursor.execute(query_one, (answer,))
                    answer_one = cursor.fetchone()
                    if answer_one:
                        answer_one_id = answer_one[0]
                        print(f"Page four, answer one ID: {answer_one_id}")
                        cursor.execute(sql, (answer_one_id, user_id, question_one_id))
                    else:
                        print("No answer found for Page four, question one")
                        return redirect(url_for('page_four.page_four_market_trends'))
                    
                for answer in page_four_question_two_answers:
                    query_two = "SELECT id FROM answers WHERE questionsId = 32 AND answer = %s"
                    cursor.execute(query_two, (answer,))
                    answer_two = cursor.fetchone()
                    if answer_two:
                        answer_two_id = answer_two[0]
                        print(f"Page four, answer two ID: {answer_two_id}")
                        cursor.execute(sql, (answer_two_id, user_id, question_two_id))
                    else:
                        print("No answer found for Page four, question two")
                        return redirect(url_for('page_four.page_four_market_trends'))
                    
                for answer in page_four_question_three_answers:
                    query_three = "SELECT id FROM answers WHERE questionsId = 33 AND answer = %s"
                    cursor.execute(query_three, (answer,))
                    answer_three = cursor.fetchone()
                    if answer_three:
                        answer_three_id = answer_three[0]
                        print(f"Page four, answer two ID: {answer_three_id}")
                        cursor.execute(sql, (answer_three_id, user_id, question_three_id))
                    else:
                        print("No answer found for Page four, question two")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_four_answers:
                    query_four = "SELECT id FROM answers WHERE questionsId = 34 AND answer = %s"
                    cursor.execute(query_four, (answer,))
                    answer_four = cursor.fetchone()
                    if answer_four:
                        answer_four_id = answer_four[0]
                        print(f"Page four, answer four ID: {answer_four_id}")
                        cursor.execute(sql, (answer_four_id, user_id, question_four_id))
                    else:
                        print("No answer found for Page four, question four")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_five_answers:
                    query_five = "SELECT id FROM answers WHERE questionsId = 35 AND answer = %s"
                    cursor.execute(query_five, (answer,))
                    answer_five = cursor.fetchone()
                    if answer_five:
                        answer_five_id = answer_five[0]
                        print(f"Page four, answer five ID: {answer_five_id}")
                        cursor.execute(sql, (answer_five_id, user_id, question_five_id))
                    else:
                        print("No answer found for Page four, question five")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_six_answers:
                    query_six = "SELECT id FROM answers WHERE questionsId = 36 AND answer = %s"
                    cursor.execute(query_six, (answer,))
                    answer_six = cursor.fetchone()
                    if answer_six:
                        answer_six_id = answer_six[0]
                        print(f"Page four, answer six ID: {answer_six_id}")
                        cursor.execute(sql, (answer_six_id, user_id, question_six_id))
                    else:
                        print("No answer found for Page four, question six")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_seven_answers:
                    query_seven = "SELECT id FROM answers WHERE questionsId = 37 AND answer = %s"
                    cursor.execute(query_seven, (answer,))
                    answer_seven = cursor.fetchone()
                    if answer_seven:
                        answer_seven_id = answer_seven[0]
                        print(f"Page four, answer seven ID: {answer_seven_id}")
                        cursor.execute(sql, (answer_seven_id, user_id, question_seven_id))
                    else:
                        print("No answer found for Page four, question seven")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_eight_answers:
                    query_eight = "SELECT id FROM answers WHERE questionsId = 38 AND answer = %s"
                    cursor.execute(query_eight, (answer,))
                    answer_eight = cursor.fetchone()
                    if answer_eight:
                        answer_eight_id = answer_eight[0]
                        print(f"Page four, answer eight ID: {answer_eight_id}")
                        cursor.execute(sql, (answer_eight_id, user_id, question_eight_id))
                    else:
                        print("No answer found for Page four, question eight")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_nine_answers:
                    query_nine = "SELECT id FROM answers WHERE questionsId = 39 AND answer = %s"
                    cursor.execute(query_nine, (answer,))
                    answer_nine = cursor.fetchone()
                    if answer_nine:
                        answer_nine_id = answer_nine[0]
                        print(f"Page four, answer nine ID: {answer_nine_id}")
                        cursor.execute(sql, (answer_nine_id, user_id, question_nine_id))
                    else:
                        print("No answer found for Page four, question nine")
                        return redirect(url_for('page_four.page_four_market_trends'))

                for answer in page_four_question_ten_answers:
                    query_ten = "SELECT id FROM answers WHERE questionsId = 40 AND answer = %s"
                    cursor.execute(query_ten, (answer,))
                    answer_ten = cursor.fetchone()
                    if answer_ten:
                        answer_ten_id = answer_ten[0]
                        print(f"Page four, answer ten ID: {answer_ten_id}")
                        cursor.execute(sql, (answer_ten_id, user_id, question_ten_id))
                    else:
                        print("No answer found for Page four, question ten")
                        return redirect(url_for('page_four.page_four_market_trends'))

                conn.commit()
                print("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                print("Failed to establish database connection")
                return redirect(url_for('page_four.page_four_market_trends'))

        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect(url_for('page_four.page_four_market_trends'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_four.page_four_market_trends'))

    print("GET Page four request received - Rendering form")
    return render_template('PageFourMarketTrends.html')
