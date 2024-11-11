from flask import Blueprint, render_template, request, redirect, url_for, session
from db_connection import create_connection, close_connection

page_one_bp = Blueprint('page_one', __name__)

@page_one_bp.route('/PageOneDigitalStrategy', methods=['GET', 'POST'])
def page_one_digital_strategy():
    print("page_one_digital_strategy inside function")
    print(request)
    if request.method == 'POST':
        print("POST request received")
        question_one = request.form.get('question-one')
        question_two = request.form.get('question-two')
        question_three = request.form.get('question-three')

        print(f"Received data - Question One: {question_one}, Question Two: {question_two}, Question Three: {question_three}")

        if 'user_id' in session:
            user_id = session['user_id']
            print(f"User ID from session: {user_id}")
        else:
            print("No user ID in session")
            return redirect(url_for('login.login'))

        try:
            conn = create_connection()
            if conn:
                print("Connection established")
                cursor = conn.cursor()

                # Retrieve the answer IDs from the answers table
                cursor.execute("SELECT id FROM answers WHERE questionsId = 1 AND answer = %s", (question_one,))
                answer_one = cursor.fetchone()
                if answer_one:
                    answer_one_id = answer_one[0]
                    print(f"Answer One ID: {answer_one_id}")
                else:
                    print("No answer found for question one")
                    return redirect(url_for('page_one.page_one_digital_strategy'))

                cursor.execute("SELECT id FROM answers WHERE questionsId = 2 AND answer = %s", (question_two,))
                answer_two = cursor.fetchone()
                if answer_two:
                    answer_two_id = answer_two[0]
                    print(f"Answer Two ID: {answer_two_id}")
                else:
                    print("No answer found for question two")
                    return redirect(url_for('page_one.page_one_digital_strategy'))

                cursor.execute("SELECT id FROM answers WHERE questionsId = 3 AND answer = %s", (question_three,))
                answer_three = cursor.fetchone()
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
