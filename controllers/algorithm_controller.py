from flask import Blueprint, session, jsonify
from db_connection import create_connection

# Create a Blueprint named 'calculate_score' for this controller
calculate_score_bp = Blueprint('calculate_score', __name__)

# Function to retrieve user answers and weights from the database
def get_user_answers_and_weights(user_id):
    conn = create_connection()  # Establish a database connection
    cursor = conn.cursor()
    # Execute a query to fetch question IDs, answers, and weights for the given user ID
    cursor.execute("""
        SELECT ua.questionsId, a.answer, a.weighting
        FROM userAnswers ua
        JOIN answers a ON ua.answersId = a.id
        WHERE ua.userId = %s
    """, (user_id,))
    answers_and_weights = cursor.fetchall()  # Fetch all results
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection
    return answers_and_weights  # Return the fetched answers and weights

# Function to calculate the score for a single section
def calculate_section_score(section_answers, section_weights):
    score = 0
    for answer, weight in zip(section_answers, section_weights):
        score += answer * weight  # Add weighted answer to the score
    return score  # Return the calculated section score

# Function to calculate the total score across all sections
def calculate_total_score(all_section_answers, all_section_weights):
    total_score = 0
    for section_answers, section_weights in zip(all_section_answers, all_section_weights):
        section_score = calculate_section_score(section_answers, section_weights)
        total_score += section_score  # Add section score to the total score
    return total_score  # Return the calculated total score

# Function to assess the total score and provide feedback
def assess_score(total_score, low_threshold, high_threshold, happy_path_range):
    if total_score < low_threshold:
        return "Score too low: Consider improving in these areas..."
    elif total_score > high_threshold:
        return "Score too high: Consider balancing your efforts..."
    elif happy_path_range[0] <= total_score <= happy_path_range[1]:
        return "Score is within the happy path: Keep up the good work!"
    else:
        return "Score is acceptable but could be optimized."

# Route to calculate and return the score and feedback
@calculate_score_bp.route('/calculate_score', methods=['GET'])
def calculate_score():
    # Check if the user is logged in
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 400

    user_id = session['user_id']  # Get user ID from session
    user_answers_and_weights = get_user_answers_and_weights(user_id)  # Fetch answers and weights

    # Create dictionaries to hold answers and weights for each section dynamically
    all_section_answers = {}
    all_section_weights = {}
    section_names = ['page_one', 'page_two', 'page_three', 'page_four', 'page_five']

    for section in section_names:
        all_section_answers[section] = []
        all_section_weights[section] = []

    # Map questions to their respective sections/pages
    for question_id, answer, weight in user_answers_and_weights:
        if 1 <= question_id <= 10:
            all_section_answers['page_one'].append(answer)
            all_section_weights['page_one'].append(weight)
        elif 11 <= question_id <= 20:
            all_section_answers['page_two'].append(answer)
            all_section_weights['page_two'].append(weight)
        elif 21 <= question_id <= 30:
            all_section_answers['page_three'].append(answer)
            all_section_weights['page_three'].append(weight)
        elif 31 <= question_id <= 40:
            all_section_answers['page_four'].append(answer)
            all_section_weights['page_four'].append(weight)
        elif 41 <= question_id <= 50:
            all_section_answers['page_five'].append(answer)
            all_section_weights['page_five'].append(weight)

    # Convert dictionary values to lists
    all_section_answers_list = list(all_section_answers.values())
    all_section_weights_list = list(all_section_weights.values())

    # Calculate the total score
    total_score = calculate_total_score(all_section_answers_list, all_section_weights_list)
    # Assess the total score and provide feedback
    feedback = assess_score(total_score, low_threshold=10, high_threshold=20, happy_path_range=(15, 18))

    # Return the total score and feedback as a JSON response
    return jsonify({"total_score": total_score, "feedback": feedback})