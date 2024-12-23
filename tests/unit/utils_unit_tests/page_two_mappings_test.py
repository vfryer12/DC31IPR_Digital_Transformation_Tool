import pytest

# Import the mappings
from controllers.utils.mappings_page_two import (
    answer_map_page_two_q1,
    answer_map_page_two_q2,
    answer_map_page_two_q3,
    answer_map_page_two_q4,
    answer_map_page_two_q5,
    answer_map_page_two_q6,
    answer_map_page_two_q7,
    answer_map_page_two_q8,
    answer_map_page_two_q9,
    answer_map_page_two_q10
)

@pytest.mark.parametrize("mapping,expected_pairs", [
    (answer_map_page_two_q1, {
        'data-analysis-answer': 'Data Analysis',
        'cybersecurity-answer': 'Cybersecurity',
        'cloud-computing-answer': 'Cloud Computing',
        'artificial-intelligence-and-machine-learning-answer': 'Artificial Intelligence and Machine Learning',
        'software-development-answer': 'Software Development',
        'project-management-answer': 'Project Management',
        'digital-marketing-answer': 'Digital Marketing',
        'ux/ui-design-answer': 'UX/UI Design',
        'remote-collaboration-tools-answer': 'Remote Collaboration Tools',
        'blockchain-technology-answer': 'Blockchain Technology'
    }),
    (answer_map_page_two_q2, {
        'skill-specific-tests-answer': 'Skill-Specific Tests',
        'certifications-and-qualifications-answer': 'Certifications and Qualifications',
        'practical-exercises-answer': 'Practical Exercises',
        'behavioral-interview-questions-answer': 'Behavioral Interview Questions',
        'online-assessments-answer': 'Online Assessments',
        'peer-review-answer': 'Peer Review',
        'hiring-via-recruiter-answer': 'Hiring via Recruiter'
    }),
    (answer_map_page_two_q3, {
        'training-programs-answer': 'Training Programs',
        'online-learning-platforms-answer': 'Online Learning Platforms',
        'workshops-and-seminars-answer': 'Workshops and Seminars',
        'learning-and-development-budget-answer': 'Learning and Development Budget',
        'mentorship-programs-answer': 'Mentorship Programs',
        'project-based-learning-answer': 'Project-Based Learning',
        'encourage-self-learning-answer': 'Encourage Self-Learning',
        'regular-assessments-and-feedback-answer': 'Regular Assessments and Feedback',
        'recognize-and-reward-learning-answer': 'Recognize and Reward Learning',
        'stay-updated-answer': 'Stay Updated'
    }),
    (answer_map_page_two_q4, {
        'leadership-support-answer': 'Leadership Support',
        'promote-a-growth-mindset-answer': 'Promote a Growth Mindset',
        'provide-learning-resources-answer': 'Provide Learning Resources',
        'learning-and-development-programs-answer': 'Learning and Development Programs',
        'encourage-self-learning-answer': 'Encourage Self-Learning',
        'regular-skill-assessments-answer': 'Regular Skill Assessments',
        'feedback-culture-answer': 'Feedback Culture',
        'recognize-and-reward-learning-answer': 'Recognize and Reward Learning',
        'create-learning-communities-answer': 'Create Learning Communities',
        'stay-updated-answer': 'Stay Updated'
    }),
    (answer_map_page_two_q5, {
        'data-analysis-q5-answer': 'Data Analysis',
        'cybersecurity-q5-answer': 'Cybersecurity',
        'cloud-computing-q5-answer': 'Cloud Computing',
        'artificial-intelligence-and-machine-learning-answer': 'Artificial Intelligence and Machine Learning',
        'software-development-answer': 'Software Development',
        'digital-marketing-answer': 'Digital Marketing',
        'ux/ui-design-answer': 'UX/UI Design',
        'project-management-answer': 'Project Management',
        'remote-collaboration-answer': 'Remote Collaboration',
        'blockchain-technology-answer': 'Blockchain Technology'
    }),
    (answer_map_page_two_q6, {
        'training-and-development-programs-answer': 'Training and Development Programs',
        'hiring-new-talent-answer': 'Hiring New Talent',
        'encouraging-continuous-learning-answer': 'Encouraging Continuous Learning',
        'leveraging-technology-answer': 'Leveraging Technology',
        'partnerships-with-educational-institutions-answer': 'Partnerships with Educational Institutions',
        'outsourcing-answer': 'Outsourcing'
    }),
    (answer_map_page_two_q7, {
        'continuous-learning-answer': 'Continuous Learning',
        'networking-answer': 'Networking',
        'following-industry-news-answer': 'Following Industry News',
        'hands-on-practice-answer': 'Hands-On Practice',
        'mentorship-answer': 'Mentorship',
        'certifications-answer': 'Certifications'
    }),
    (answer_map_page_two_q8, {
        'skills-assessment-answer': 'Skills Assessment',
        'training-and-development-q8-answer': 'Training and Development',
        'hiring-strategy-answer': 'Hiring Strategy',
        'encourage-continuous-learning-answer': 'Encourage Continuous Learning',
        'leverage-technology-answer': 'Leverage Technology',
        'partnerships-answer': 'Partnerships'
    }),
    (answer_map_page_two_q9, {
        'already-doing-the-listed-options-answer': 'Already doing the listed options',
        'training-and-development-answer': 'Training and Development',
        'support-and-resources-answer': 'Support and Resources',
        'culture-of-adaptability-answer': 'Culture of Adaptability',
        'pilot-testing-answer': 'Pilot Testing',
        'feedback-mechanisms-answer': 'Feedback Mechanisms',
        'leadership-involvement-answer': 'Leadership Involvement'
    }),
    (answer_map_page_two_q10, {
        'already-doing-the-listed-options-answer': 'Already doing the listed options',
        'competitive-compensation-answer': 'Competitive Compensation',
        'career-development-opportunities-answer': 'Career Development Opportunities',
        'continuous-learning-and-development-answer': 'Continuous Learning and Development',
        'workplace-culture-answer': 'Workplace Culture',
        'flexible-work-arrangements-answer': 'Flexible Work Arrangements',
        'interesting-projects-answer': 'Interesting Projects',
        'employer-branding-answer': 'Employer Branding'
    })
])
def test_positive_mappings(mapping, expected_pairs):
    """
    Test that each mapping contains all expected key-value pairs.
    """
    for key, value in expected_pairs.items():
        assert key in mapping, f"Key {key} is missing from the mapping."
        assert mapping[key] == value, f"Key {key} has incorrect value. Expected {value}, got {mapping[key]}."

# Negative tests
@pytest.mark.parametrize("mapping,unexpected_keys,unexpected_values", [
    (answer_map_page_two_q1,
     ['invalid-key-1', 'fake-key'], 
     ['Invalid Value 1', 'Fake Value']),
    (answer_map_page_two_q2,
     ['unknown-key', 'unmapped-key'], 
     ['Unknown Value', 'Unmapped Value']),
    (answer_map_page_two_q3,
     ['wrong-key', 'dummy-key'], 
     ['Wrong Value', 'Dummy Value']),
    (answer_map_page_two_q4,
     ['error-key', 'nonexistent-key'], 
     ['Error Value', 'Nonexistent Value']),
    (answer_map_page_two_q5,
     ['placeholder-key', 'example-key'], 
     ['Placeholder Value', 'Example Value']),
    (answer_map_page_two_q6,
     ['bogus-key', 'nonsense-key'], 
     ['Bogus Value', 'Nonsense Value']),
    (answer_map_page_two_q7,
     ['irrelevant-key', 'unused-key'], 
     ['Irrelevant Value', 'Unused Value']),
    (answer_map_page_two_q8,
     ['test-key', 'invalid-entry'], 
     ['Test Value', 'Invalid Entry']),
    (answer_map_page_two_q9,
     ['nonexistent-id', 'invalid-key'], 
     ['Nonexistent Value', 'Invalid Key']),
    (answer_map_page_two_q10,
     ['missing-key', 'fake-id'], 
     ['Missing Value', 'Fake ID']),
])
def test_page_two_negative_mappings(mapping, unexpected_keys, unexpected_values):
    """
    Negative tests to ensure mappings do not include unexpected keys or values.
    """
    # Ensure unexpected keys are NOT in the mapping
    for key in unexpected_keys:
        assert key not in mapping, f"Unexpected key {key} found in the mapping."

    # Ensure unexpected values are NOT in the mapping
    for value in unexpected_values:
        assert value not in mapping.values(), f"Unexpected value {value} found in the mapping."

