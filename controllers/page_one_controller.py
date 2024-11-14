from flask import Blueprint, render_template, request, redirect, url_for, session
from db_connection import create_connection, close_connection

page_one_bp = Blueprint('page_one', __name__)

@page_one_bp.route('/PageOneDigitalStrategy', methods=['GET', 'POST'])
def page_one_digital_strategy():
    print("page_one_digital_strategy inside function")
    print(request)
    if request.method == 'POST':
        print("POST request received")
        
        # Get form data
        question_one_value = request.form.get('question-one')
        question_two_value = request.form.get('question-two')
        question_three_value = request.form.get('question-three')

        print(f"Received data - Question One: {question_one_value}, Question Two: {question_two_value}, Question Three: {question_three_value}")

        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
            return redirect(url_for('login.login'))

        # Map form values to database values for question one
        answer_map_q1 = {
            '1': 'No plan in place',
            '2': 'Needs Improvement',
            '3': 'Fully Aligned'
        }

        # Mapping for question two
        answer_map_q2 = {
            'cio': 'Chief Information Officer (CIO)',
            'cto': 'Chief Technology Officer (CTO)',
            'dtm': 'Digital Transformation Manager',
            'cdo': 'Chief Digital Officer (CDO)',
            'itd': 'IT Director/Manager',
            'bul': 'Business Unit Leader',
            'md': 'Marketing Director',
            'dal': 'Data Analytics Leader',
            'other': 'Other'
        }

        # Mapping for question three
        answer_map_q3 = {
            'never': 'Never',
            'monthly': 'Every Month',
            'quarterly': 'Quarterly',
            'year': 'Annually',
            'continuous': 'Continuous'
        }

        # Ensure the form values are correctly mapped
        question_one_answer = answer_map_q1.get(question_one_value, None)
        question_two_answer = answer_map_q2.get(question_two_value, None)
        question_three_answer = answer_map_q3.get(question_three_value, None)

        if not question_one_answer:
            print("Invalid answer for question one")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_two_answer:
            print("Invalid answer for question two")
            return redirect(url_for('page_one.page_one_digital_strategy'))

        if not question_three_answer:
            print("Invalid answer for question three")
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

                question_one_id = 1
                question_two_id = 2
                question_three_id = 3

                # Insert data into the userAnswers table
                sql = "INSERT INTO userAnswers (answersId, userId, questionsId) VALUES (%s, %s, %s)"
                cursor.execute(sql, (answer_one_id, user_id, question_one_id))
                cursor.execute(sql, (answer_two_id, user_id, question_two_id))
                cursor.execute(sql, (answer_three_id, user_id, question_three_id))

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

    print("GET request received - Rendering form")
    return render_template('PageOneDigitalStrategy.html')