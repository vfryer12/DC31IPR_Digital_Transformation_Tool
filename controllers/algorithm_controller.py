# algorithm_controller.py

from flask import Blueprint, session, jsonify, request
from db_connector import create_connection
from daos.get_user_answer_weights import get_user_answer_weights

# Create a Blueprint named 'calculate_score' for this controller
calculate_score_bp = Blueprint('calculate_score', __name__)

# Function to retrieve user answers and weights from the database
def get_user_weights(user_id):
    # Establish a database connection
    conn = create_connection()
    cursor = conn.cursor()
    # Execute a query to fetch question IDs and weights for the given user ID
    user_weights = get_user_answer_weights(cursor, user_id)
    # Close the cursor
    cursor.close()
    # Close the database connection
    conn.close()
    # Return the fetched weights
    return user_weights

# Function to calculate the total score across all sections
def calculate_total_weight(all_section_weights):
    total_score = 0
    for section_weights in all_section_weights:
        # Sum up all weights in each section
        total_score += sum(section_weights)
    # Return the calculated total score
    return total_score

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


@calculate_score_bp.route('/calculate_score', methods=['GET'])
def calculate_score():
    """
    Retrieve user data and calculate the score.
    """
    # Check if the user is logged in
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 400

    user_id = session['user_id']
    conn = create_connection()
    cursor = conn.cursor()

    user_weights = get_user_answer_weights(cursor, user_id)

    cursor.close()
    conn.close()

    # Calculate the total score
    total_score = sum(weight for _, weight in user_weights)
    feedback = "Score is within the happy path: Keep up the good work!" if total_score >= 15 else "Consider improving."

    # Return JSON response or render a page with results
    return jsonify({"total_score": total_score, "feedback": feedback})