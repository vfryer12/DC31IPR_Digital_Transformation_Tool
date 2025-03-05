# algorithm_controller.py

from db_connector import create_connection
from daos import get_db_data
from flask import Blueprint, jsonify, session, render_template
from collections import defaultdict

# Create a Blueprint named 'calculate_score' for this controller
calculate_score_bp = Blueprint('calculate_score', __name__)

# Define thresholds for each section based on the data
SECTION_THRESHOLDS = {
    "Digital Strategy": {"happy_path": 30, "pain_path": 138, "median": 84},
    "Digital Skills": {"happy_path": 60, "pain_path": 207, "median": 133.5},
    "Technology Adoption": {"happy_path": 58, "pain_path": 239, "median": 148.5},
    "Market Trends": {"happy_path": 30, "pain_path": 154, "median": 92},
    "Digital Marketing": {"happy_path": 35, "pain_path": 185, "median": 110}
}

# Overall thresholds
OVERALL_THRESHOLDS = {
    "happy_path_total": 213,
    "pain_path_total": 923,
    "median_total": 113.6
}

# Function to assess individual section scores
def assess_section_score(section, score):
    thresholds = SECTION_THRESHOLDS[section]
    if score < thresholds["happy_path"]:
        return f"{section}: Score too low. Consider improving in this area."
    elif score > thresholds["pain_path"]:
        return f"{section}: Score too high. Balance efforts in this area."
    elif thresholds["happy_path"] <= score <= thresholds["median"]:
        return f"{section}: Score is within the happy path. Good work!"
    else:
        return f"{section}: Score is acceptable but could be optimized."

# Function to assess overall score
def assess_overall_score(total_score):
    if total_score < OVERALL_THRESHOLDS["happy_path_total"]:
        return "Overall: Total score is too low. Improvement needed across sections."
    elif total_score > OVERALL_THRESHOLDS["pain_path_total"]:
        return "Overall: Total score is too high. Balance efforts across sections."
    elif OVERALL_THRESHOLDS["happy_path_total"] <= total_score <= OVERALL_THRESHOLDS["median_total"]:
        return "Overall: Total score is within the happy path. Keep it up!"
    else:
        return "Overall: Total score is acceptable but could be optimized."

# Function to calculate distance from median for k-NN analysis
def calculate_knn_distance(section, score):
    thresholds = SECTION_THRESHOLDS[section]
    median = thresholds["median"]
    distance = abs(score - median)
    return distance

# Function to find k-nearest sections by score
def find_knn_sections(user_scores, k=5):
    distances = {
        section: calculate_knn_distance(section, score)
        for section, score in user_scores.items()
    }
    # Sort sections by distance from median and select top-k
    sorted_sections = sorted(distances.items(), key=lambda x: x[1], reverse=True)
    return [
        {"section": section, "distance": distance}
        for section, distance in sorted_sections[:k]
    ]

def format_solution(sol_text: str):
    return sol_text.removesuffix(".") + "."

@calculate_score_bp.route('/calculate_score', methods=['GET'])
def calculate_score():

    # Check if the user is logged in
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 400

    user_id = session['user_id']

    # Retrieve user weights from the database
    conn = create_connection()
    user_answer_weights = get_db_data.get_section_answer_weights(conn, user_id)
    user_answer_solutions = get_db_data.get_answer_solutions(conn, user_id)

    question_set = set()
    # Iterate through each row in the user_answer_solutions list
    for row in user_answer_solutions:
        # Add a tuple containing section ID, question ID, and the question itself to the question_set
        question_set.add(tuple([row.sectionid, row.questionsid, row.question]))

    section_info = {}
    # Iterate through each unique question tuple in question_set
    for q in question_set:
        sols = [format_solution(row.solution) for row in user_answer_solutions if row.questionsid == q[1]]
        # Map the current question tuple to its corresponding list of solutions    
        section_info[q] = sols

    conn.close()

    unique_section_names = list(set([i[0] for i in user_answer_weights]))

    section_weight_dict = {section_name: 0 for section_name in unique_section_names}
    
    for section_name, _, weight in user_answer_weights:
        section_weight_dict[section_name]+=weight

    # Calculate section-wise feedback
    section_feedback = {
        section: assess_section_score(section, score)
        for section, score in section_weight_dict.items()
    }

    user_weight_list = [i[-1] for i in user_answer_weights]

    # Calculate total score
    total_score = sum(user_weight_list)

    # Assess overall score
    overall_feedback = assess_overall_score(total_score)

    # Find k-nearest sections
    user_weights = {k:v for k,_,v in user_answer_weights}
    knn_sections = find_knn_sections(user_weights, k=5)

    return render_template(
        "ReportPage.html",
        total_score=total_score,
        overall_feedback=overall_feedback,
        section_feedback=section_feedback,
        knn_sections=knn_sections,
        user_scores=section_weight_dict,
        recommended_solutions=section_info
    )
