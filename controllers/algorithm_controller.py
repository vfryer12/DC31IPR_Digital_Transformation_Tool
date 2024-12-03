from flask import Blueprint, session, jsonify
from db_connection import create_connection

# Create a Blueprint named 'calculate_score' for this controller
calculate_score_bp = Blueprint('calculate_score', __name__)

# Function to retrieve user answers and weights from the database
def get_user_weights(user_id):
    conn = create_connection()  # Establish a database connection
    cursor = conn.cursor()
    # Execute a query to fetch question IDs and weights for the given user ID
    cursor.execute("""
        SELECT ua.questionsId, a.weighting
        FROM userAnswers ua
        JOIN answers a ON ua.answersId = a.id
        WHERE ua.userId = %s
    """, (user_id,))
    weights = cursor.fetchall()  # Fetch all results
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection
    return weights  # Return the fetched weights

# Function to calculate the total score across all sections
def calculate_total_weight(all_section_weights):
    total_score = 0
    for section_weights in all_section_weights:
        total_score += sum(section_weights)  # Sum up all weights in each section
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
    user_weights = get_user_weights(user_id)  # Fetch weights

    # Debugging print to verify retrieved data
    print("Retrieved weights:", user_weights)

    # Create dictionaries to hold weights for each section dynamically
    all_section_weights = {}
    section_names = ['page_one', 'page_two', 'page_three', 'page_four', 'page_five']

    for section in section_names:
        all_section_weights[section] = []

    # Map weights to their respective sections/pages
    for question_id, weight in user_weights:
        print(f"Question ID: {question_id}, Weight: {weight}")  # Debugging print
        if 1 <= question_id <= 10:
            all_section_weights['page_one'].append(weight)
        elif 11 <= question_id <= 20:
            all_section_weights['page_two'].append(weight)
        elif 21 <= question_id <= 30:
            all_section_weights['page_three'].append(weight)
        elif 31 <= question_id <= 40:
            all_section_weights['page_four'].append(weight)
        elif 41 <= question_id <= 50:
            all_section_weights['page_five'].append(weight)

    # Debugging print to verify mapping
    print("Section weights:", all_section_weights)

    # Convert dictionary values to lists
    all_section_weights_list = list(all_section_weights.values())

    # Debugging print to verify list conversion
    print("Section weights list:", all_section_weights_list)

    # Calculate the total weight
    total_score = calculate_total_weight(all_section_weights_list)
    # Debugging print to verify total score
    print("Total score:", total_score)

    # Assess the total score and provide feedback
    feedback = assess_score(total_score, low_threshold=10, high_threshold=20, happy_path_range=(15, 18))
    print("Feedback:", feedback)  # Debugging print

    # Return the total score and feedback as a JSON response
    return jsonify({"total_score": total_score, "feedback": feedback})