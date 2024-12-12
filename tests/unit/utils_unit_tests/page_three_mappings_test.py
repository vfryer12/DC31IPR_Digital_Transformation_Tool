import pytest

# Import the mappings
from controllers.utils.mappings_page_three import (
    answer_map_page_three_q1,
    answer_map_page_three_q2,
    answer_map_page_three_q3,
    answer_map_page_three_q4,
    answer_map_page_three_q5,
    answer_map_page_three_q6,
    answer_map_page_three_q7,
    answer_map_page_three_q8,
    answer_map_page_three_q9,
    answer_map_page_three_q10
)

# Positive tests
@pytest.mark.parametrize("mapping,expected_pairs", [
    (answer_map_page_three_q1, {
        'define-clear-objectives-answer': 'Define Clear Objectives',
        'assess-alignment-with-your-business-answer': 'Assess Alignment with Your Business',
        'feasibility-and-viability-check-answer': 'Feasibility and Viability Check',
        'risk-analysis-answer': 'Risk Analysis',
        'performance-against-KPIs-answer': 'Performance Against KPIs',
        'test-and-iterate-answer': 'Test and Iterate',
        'explore-market-potential-answer': 'Explore Market Potential',
        'collaborate-and-seek-expert-input-answer': 'Collaborate and Seek Expert Input',
        'user-friendliness-answer': 'User-Friendliness',
        'long-term-vision-assessmentg-answer': 'Long-Term Vision Assessment'
    }),
    (answer_map_page_three_q2, {
        'clear-communication-answer': 'Clear Communication',
        'leadership-support-answer': 'Leadership Support',
        'comprehensive-training-programs-answer': 'Comprehensive Training Programs',
        'change-management-strategies-answer': 'Change Management Strategies',
        'user-friendly-design-answer': 'User-Friendly Design',
        'support-systems-answer': 'Support Systems',
        'pilot-testing-answer': 'Pilot Testing',
        'gradual-implementation-answer': 'Gradual Implementation',
        'feedback-mechanisms-answer': 'Feedback Mechanisms',
        'monitor-and-evaluate-answer': 'Monitor and Evaluate'
    }),
    (answer_map_page_three_q3, {
        'resistance-to-change-answer': 'Resistance to Change',
        'lack-of-skilled-personnel-answer': 'Lack of Skilled Personnel',
        'complexity-of-technology-answer': 'Complexity of Technology',
        'security-concerns-answer': 'Security Concerns',
        'budget-constraints-answer': 'Budget Constraints',
        'inadequate-training-answer': 'Inadequate Training',
        'cultural-mindset-answer': 'Cultural Mindset',
        'siloed-organizational-structure-answer': 'Siloed Organizational Structure',
        'continuous-evolution-of-customer-needs-answer': 'Continuous Evolution of Customer Needs',
        'measuring-ROI-answer': 'Measuring ROI'
    }),
    (answer_map_page_three_q4, {
        'user-adoption-rate-answer': 'User Adoption Rate',
        'performance-metrics-answer': 'Performance Metrics',
        'return-on-investment-answer': 'Return on Investment (ROI)',
        'user-satisfaction-answer': 'User Satisfaction',
        'usage-frequency-answer': 'Usage Frequency',
        'business-impact-answer': 'Business Impact',
        'time-to-proficiency-answer': 'Time to Proficiency',
        'support-requests-answer': 'Support Requests',
        'feature-adoption-rate-answer': 'Feature Adoption Rate',
        'training-completion-rates-answer': 'Training Completion Rates'
    }),
    (answer_map_page_three_q5, {
        'define-clear-business-goals-answer': 'Define Clear Business Goals',
        'collaborate-with-stakeholders-answer': 'Collaborate with Stakeholders',
        'conduct-a-needs-assessment-answer': 'Conduct a Needs Assessment',
        'develop-a-unified-strategy-answer': 'Develop a Unified Strategy',
        'monitor-and-measure-performance-answer': 'Monitor and Measure Performance',
        'data-driven-decision-making-answer': 'Data-Driven Decision Making',
        'implement-governance-and-accountability-answer': 'Implement Governance and Accountability',
        'continuous-feedback-loops-answer': 'Continuous Feedback Loops',
        'encourage-cross-functional-collaboration-answer': 'Encourage Cross-Functional Collaboration',
        'adapt-and-evolve-answer': 'Adapt and Evolve'
    }),
    (answer_map_page_three_q6, {
        'set-and-communicate-clear-goals-answer': 'Set and Communicate Clear Goals',
        'develop-a-comprehensive-strategy-answer': 'Develop a Comprehensive Strategy',
        'provide-continuous-training-and-support-answer': 'Provide Continuous Training and Support',
        'build-a-dedicated-change-management-team-answer': 'Build a Dedicated Change Management Team',
        'plan-for-resistance-answer': 'Plan for Resistance',
        'encourage-employee-involvement-answer': 'Encourage Employee Involvement',
        'monitor-and-evaluate-progress-answer': 'Monitor and Evaluate Progress',
        'communicate-regularly-answer': 'Communicate Regularly',
        'foster-a-culture-of-innovationn-answer': 'Foster a Culture of Innovation',
        'celebrate-successes-answer': 'Celebrate Successes'
    }),
    (answer_map_page_three_q7, {
        'join-professional-organizations-answer': 'Join Professional Organizations',
        'attend-industry-conferences-and-tech-events-answer': 'Attend Industry Conferences and Tech Events',
        'follow-tech-news-and-blogs-answer': 'Follow Tech News and Blogs',
        'engage-on-social-media-answer': 'Engage on Social Media',
        'take-online-courses-and-webinars-answer': 'Take Online Courses and Webinars',
        'network-with-peers-answer': 'Network with Peers',
        'find-a-mentor-answer': 'Find a Mentor',
        'watch-TED-talks-and-tech-videos-answer': 'Watch TED Talks and Tech Videos',
        'participate-in-online-forums-and-communities-answer': 'Participate in Online Forums and Communities',
        'read-industry-reports-and-whitepapers-answer': 'Read Industry Reports and Whitepapers'
    }),
    (answer_map_page_three_q8, {
        'regularly-review-and-update-answer': 'Regularly Review and Update',
        'stay-informed-on-industry-trends-answer': 'Stay Informed on Industry Trends',
        'implement-continuous-integration-and-deployment-answer': 'Implement Continuous Integration and Deployment (CI/CD)',
        'conduct-regular-audits-answer': 'Conduct Regular Audits',
        'engage-with-the-developer-community-answer': 'Engage with the Developer Community',
        'foster-a-culture-of-learning-answer': 'Foster a Culture of Learning',
        'collaborate-with-vendors-and-partners-answer': 'Collaborate with Vendors and Partners',
        'adopt-modular-architecture-answer': 'Adopt Modular Architecture',
        'monitor-and-analyze-performance-answer': 'Monitor and Analyze Performance',
        'plan-for-scalability-and-future-growth-answer': 'Plan for Scalability and Future Growth'
    }),
    (answer_map_page_three_q9, {
        'conduct-a-comprehensive-risk-assessment-answer': 'Conduct a Comprehensive Risk Assessment',
        'develop-a-risk-mitigation-plan-answer': 'Develop a Risk Mitigation Plan',
        'perform-a-cost-benefit-analysis-answer': 'Perform a Cost-Benefit Analysis',
        'conduct-cybersecurity-assessments-answer': 'Conduct Cybersecurity Assessments',
        'implement-pilot-testing-answer': 'Implement Pilot Testing',
        'monitor-regulatory-compliance-answer': 'Monitor Regulatory Compliance',
        'engage-with-stakeholders-answer': 'Engage with Stakeholders',
        'analyze-historical-data-answer': 'Analyze Historical Data',
        'use-risk-assessment-tools-answer': 'Use Risk Assessment Tools',
        'seek-expert-consultation-answer': 'Seek Expert Consultation'
    }),
    (answer_map_page_three_q10, {
        'communicate-the-benefits-answer': 'Communicate the Benefits',
        'involve-employees-early-answer': 'Involve Employees Early',
        'provide-comprehensive-training-answer': 'Provide Comprehensive Training',
        'address-concerns-openly-answer': 'Address Concerns Openly',
        'implement-change-management-strategies-answer': 'Implement Change Management Strategies',
        'foster-a-positive-culture-answer': 'Foster a Positive Culture',
        'provide-ongoing-support-answer': 'Provide Ongoing Support',
        'showcase-success-stories-answer': 'Showcase Success Stories',
        'offer-incentive-answer': 'Offer Incentive',
        'monitor-and-adjust-answer': 'Monitor and Adjust'
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
    (answer_map_page_three_q1,
     ['invalid-key-1', 'fake-key'], 
     ['Invalid Value 1', 'Fake Value']),
    (answer_map_page_three_q2,
     ['unknown-key', 'unmapped-key'], 
     ['Unknown Value', 'Unmapped Value']),
    (answer_map_page_three_q3,
     ['wrong-key', 'dummy-key'], 
     ['Wrong Value', 'Dummy Value']),
    (answer_map_page_three_q4,
     ['error-key', 'nonexistent-key'], 
     ['Error Value', 'Nonexistent Value']),
    (answer_map_page_three_q5,
     ['placeholder-key', 'example-key'], 
     ['Placeholder Value', 'Example Value']),
    (answer_map_page_three_q6,
     ['bogus-key', 'nonsense-key'], 
     ['Bogus Value', 'Nonsense Value']),
    (answer_map_page_three_q7,
     ['irrelevant-key', 'unused-key'], 
     ['Irrelevant Value', 'Unused Value']),
    (answer_map_page_three_q8,
     ['test-key', 'invalid-entry'], 
     ['Test Value', 'Invalid Entry']),
    (answer_map_page_three_q9,
     ['nonexistent-id', 'invalid-key'], 
     ['Nonexistent Value', 'Invalid Key']),
    (answer_map_page_three_q10,
     ['missing-key', 'fake-id'], 
     ['Missing Value', 'Fake ID']),
])
def test_page_three_negative_mappings(mapping, unexpected_keys, unexpected_values):
    """
    Negative tests to ensure mappings do not include unexpected keys or values.
    """
    # Ensure unexpected keys are NOT in the mapping
    for key in unexpected_keys:
        assert key not in mapping, f"Unexpected key {key} found in the mapping."

    # Ensure unexpected values are NOT in the mapping
    for value in unexpected_values:
        assert value not in mapping.values(), f"Unexpected value {value} found in the mapping."
