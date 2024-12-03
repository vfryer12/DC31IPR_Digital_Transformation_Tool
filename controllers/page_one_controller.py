from flask import Blueprint, render_template, request, redirect, url_for, session
from db_connection import create_connection, close_connection
from controllers.utils.mappings_page_one import answer_map_q1, answer_map_q2, answer_map_q3, answer_map_q4, answer_map_q5, answer_map_q6, answer_map_q7, answer_map_q8, answer_map_q9, answer_map_q10

page_one_bp = Blueprint('page_one', __name__)

@page_one_bp.route('/PageOneDigitalStrategy', methods=['GET', 'POST'])

def page_one_digital_strategy():
    print("page_one_digital_strategy inside function")
    print(request)
    if request.method == 'POST':
        print("POST page one request received")
        
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

        print(f"Received data - Question One: {question_one_values}, Question Two: {question_two_values}, Question Three: {question_three_values}, Question Four: {question_four_values}, Question Five: {question_five_values}, Question Six: {question_six_values}, Question Seven: {question_seven_values}, Question Eight: {question_eight_values}, Question Nine: {question_nine_values}, Question Ten: {question_ten_values}")


        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
            return redirect(url_for('login.login'))

        # Ensure the form values are correctly mapped
        question_one_answer    = [answer_map_q1.get(value, None) for value in question_one_values]
        question_two_answer    = [answer_map_q2.get(value, None) for value in question_two_values]
        question_three_answer  = [answer_map_q3.get(value, None) for value in question_three_values]
        question_four_answers  = [answer_map_q4.get(value, None) for value in question_four_values]
        question_five_answers  = [answer_map_q5.get(value, None) for value in question_five_values]
        question_six_answers   = [answer_map_q6.get(value, None) for value in question_six_values]
        question_seven_answers = [answer_map_q7.get(value, None) for value in question_seven_values]
        question_eight_answers = [answer_map_q8.get(value, None) for value in question_eight_values]
        question_nine_answers  = [answer_map_q9.get(value, None) for value in question_nine_values]
        question_ten_answers   = [answer_map_q10.get(value, None) for value in question_ten_values]
        
        if not question_one_answer:
            print("Invalid answer for question one")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_two_answer:
            print("Invalid answer for question two")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_three_answer:
            print("Invalid answer for question three")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if None in question_four_answers:
            print("Invalid answer for question four")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if len(question_five_answers) > 3 or None in question_five_answers:
            print("Invalid answer for question five or more than three selections made")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if None in question_six_answers:
            print("Invalid answer for question six")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if None in question_seven_answers:
            print("Invalid answer for question seven")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if None in question_eight_answers:
            print("Invalid answer for question eight")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if None in question_nine_answers:
            print("Invalid answer for question nine")
            return redirect(url_for('page_one.page_one_digital_strategy'))
        
        if None in question_ten_answers:
            print("Invalid answer for question ten")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        try:
            conn = create_connection()
            if conn:
                print("Connection established")
                cursor = conn.cursor()

                # Debugging the SQL queries
                query_one = "SELECT id FROM answers WHERE questionsId = 1 AND answer = %s"
                cursor.execute(query_one, (question_one_answer,))
                answer_one = cursor.fetchone()
                print(f"Query for Question One: {query_one % question_one_answer}, Result: {answer_one}")
                if answer_one:
                    answer_one_id = answer_one[0]
                    print(f"Answer One ID: {answer_one_id}")
                else:
                    print("No answer found for question one")
                    return redirect(url_for('page_one.page_one_digital_strategy'))

                query_two = "SELECT id FROM answers WHERE questionsId = 2 AND answer = %s"
                cursor.execute(query_two, (question_two_answer,))
                answer_two = cursor.fetchone()
                print(f"Query for Question Two: {query_two % question_two_answer}, Result: {answer_two}")
                if answer_two:
                    answer_two_id = answer_two[0]
                    print(f"Answer Two ID: {answer_two_id}")
                else:
                    print("No answer found for question two")
                    return redirect(url_for('page_one.page_one_digital_strategy'))

                query_three = "SELECT id FROM answers WHERE questionsId = 3 AND answer = %s"
                cursor.execute(query_three, (question_three_answer,))
                answer_three = cursor.fetchone()
                print(f"Query for Question Three: {query_three % question_three_answer}, Result: {answer_three}")
                if answer_three:
                    answer_three_id = answer_three[0]
                    print(f"Answer Three ID: {answer_three_id}")
                else:
                    print("No answer found for question three")
                    return redirect(url_for('page_one.page_one_digital_strategy'))
                
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

                # Insert data into the userAnswers table
                sql = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"
                cursor.execute(sql, (answer_one_id, user_id, question_one_id))
                cursor.execute(sql, (answer_two_id, user_id, question_two_id))
                cursor.execute(sql, (answer_three_id, user_id, question_three_id))

                for answer in question_four_answers:
                    query_four = "SELECT id FROM answers WHERE questionsId = 4 AND answer = %s"
                    cursor.execute(query_four, (answer,))
                    answer_four = cursor.fetchone()
                    if answer_four:
                        answer_four_id = answer_four[0]
                        print(f"Answer Four ID: {answer_four_id}")
                        cursor.execute(sql, (answer_four_id, user_id, question_four_id))
                    else:
                        print("No answer found for question four")
                        return redirect(url_for('page_one.page_one_digital_strategy'))


                for answer in question_five_answers:
                    query_five = "SELECT id FROM answers WHERE questionsId = 5 AND answer = %s"
                    cursor.execute(query_five, (answer,))
                    answer_five = cursor.fetchone()
                    if answer_five:
                        answer_five_id = answer_five[0]
                        print(f"Answer Five ID: {answer_five_id}")
                        cursor.execute(sql, (answer_five_id, user_id, question_five_id))
                    else:
                        print("No answer found for question five")
                        return redirect(url_for('page_one.page_one_digital_strategy'))

                    
                for answer in question_six_answers:
                    query_six = "SELECT id FROM answers WHERE questionsId = 6 AND answer = %s"
                    cursor.execute(query_six, (answer,))
                    answer_six = cursor.fetchone()
                    if answer_six:
                        answer_six_id = answer_six[0]
                        print(f"Answer Six ID: {answer_six_id}")
                        cursor.execute(sql, (answer_six_id, user_id, question_six_id))
                    else:
                        print("No answer found for question six")
                        return redirect(url_for('page_one.page_one_digital_strategy'))
                    
                # Handle question seven answers
                for answer in question_seven_answers:
                    query_seven = "SELECT id FROM answers WHERE questionsId = 7 AND answer = %s"
                    cursor.execute(query_seven, (answer,))
                    answer_seven = cursor.fetchone()
                    if answer_seven:
                        answer_seven_id = answer_seven[0]
                        print(f"Answer Seven ID: {answer_seven_id}")
                        cursor.execute(sql, (answer_seven_id, user_id, question_seven_id))
                    else:
                        print("No answer found for question seven")
                        return redirect(url_for('page_one.page_one_digital_strategy'))
                
                # Handle question eight answers
                for answer in question_eight_answers:
                    query_eight = "SELECT id FROM answers WHERE questionsId = 8 AND answer = %s"
                    cursor.execute(query_eight, (answer,))
                    answer_eight = cursor.fetchone()
                    if answer_eight:
                        answer_eight_id = answer_eight[0]
                        print(f"Answer Eight ID: {answer_eight_id}")
                        cursor.execute(sql, (answer_eight_id, user_id, question_eight_id))
                    else:
                        print("No answer found for question eight")
                        return redirect(url_for('page_one.page_one_digital_strategy'))
                
                # Handle question nine answers
                for answer in question_nine_answers:
                    query_nine = "SELECT id FROM answers WHERE questionsId = 9 AND answer = %s"
                    cursor.execute(query_nine, (answer,))
                    answer_nine = cursor.fetchone()
                    if answer_nine:
                        answer_nine_id = answer_nine[0]
                        print(f"Answer Nine ID: {answer_nine_id}")
                        cursor.execute(sql, (answer_nine_id, user_id, question_nine_id))
                    else:
                        print("No answer found for question nine")
                        return redirect(url_for('page_one.page_one_digital_strategy'))
                    
                # Handle question ten answers
                for answer in question_ten_answers:
                    query_ten = "SELECT id FROM answers WHERE questionsId = 10 AND answer = %s"
                    cursor.execute(query_ten, (answer,))
                    answer_ten = cursor.fetchone()
                    if answer_ten:
                        answer_ten_id = answer_ten[0]
                        print(f"Answer Ten ID: {answer_ten_id}")
                        cursor.execute(sql, (answer_ten_id, user_id, question_ten_id))
                    else:
                        print("No answer found for question ten")
                        return redirect(url_for('page_one.page_one_digital_strategy'))

                conn.commit()
                print("Successfully inserted data into userAnswers table")

                cursor.close()
            else:
                print("Failed to establish database connection")
                return redirect(url_for('page_one.page_one_digital_strategy'))

        except Exception as e:
            print(f"An error occurred: {e}")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        finally:
            close_connection(conn)

        return redirect(url_for('page_one.page_one_digital_strategy'))

    print("GET page one request received - Rendering form")
    return render_template('PageOneDigitalStrategy.html')