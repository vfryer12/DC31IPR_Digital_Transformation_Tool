import pytest

from controllers.utils.mappings_page_four import (
    answer_map_page_four_q1,
    answer_map_page_four_q2,
    answer_map_page_four_q3,
    answer_map_page_four_q4,
    answer_map_page_four_q5,
    answer_map_page_four_q6,
    answer_map_page_four_q7,
    answer_map_page_four_q8,
    answer_map_page_four_q9,
    answer_map_page_four_q10
)


@pytest.mark.parametrize("mapping,expected_pairs", [
    (answer_map_page_four_q1, {
        'market-research-and-analysis-answer': 'Market Research and Analysis',
        'customer-feedback-and-insights-answer': 'Customer Feedback and Insights',
        'networking-and-conferences-answer': 'Networking and Conferences',
        'professional-organizations-answer': 'Professional Organizations',
        'regular-industry-reading-answer': 'Regular Industry Reading',
        'social-media-monitoring-answer': 'Social Media Monitoring',
        'technology-tools-and-alerts-answer': 'Technology Tools and Alerts',
        'internal-knowledge-sharing-answer': 'Internal Knowledge Sharing',
        'online-courses-and-certifications-answer': 'Online Courses and Certifications',
        'mentorship-and-collaboration-answer': 'Mentorship and Collaboration'
    }),
    (answer_map_page_four_q2, {
        'data-driven-decision-making-answer': 'Data-Driven Decision Making',
        'enhanced-customer-experience-answer': 'Enhanced Customer Experience',
        'agility-and-adaptability-answer': 'Agility and Adaptability',
        'innovation-and-competitive-edge-answer': 'Innovation and Competitive Edge',
        'accelerated-digital-transformation-answer': 'Accelerated Digital Transformation',
        'operational-efficiency-answer': 'Operational Efficiency',
        'employee-empowerment-answer': 'Employee Empowerment',
        'sustainability-initiatives-answer': 'Sustainability Initiatives'
    }),
    (answer_map_page_four_q3, {
        'adopting-AI-and-machine-learning-answer': 'Adopting AI and Machine Learning',
        'investing-in-data-analytics-answer': 'Investing in Data Analytics',
        'enhancing-cybersecurity-measures-answer': 'Enhancing Cybersecurity Measures',
        'embracing-cloud-computing-answer': 'Embracing Cloud Computing',
        'developing-digital-products-and-services-answer': 'Developing Digital Products and Services',
        'implementing-IoT-solutions-answer': 'Implementing IoT Solutions',
        'collaborating-with-tech-partners-answer': 'Collaborating with Tech Partners',
        'fostering-a-culture-of-innovation-answer': 'Fostering a Culture of Innovation',
        'exploring-blockchain-technology-answer': 'Exploring Blockchain Technology',
        'sustainability-through-digital-solutions-answer': 'Sustainability through Digital Solutions'
    }),
    (answer_map_page_four_q4, {
        'leveraging-data-and-analytics-answer': 'Leveraging Data and Analytics',
        'continuous-market-analysis-answer': 'Continuous Market Analysis',
        'customer-feedback-integration-answer': 'Customer Feedback Integration',
        'agile-methodologies-answer': 'Agile Methodologies',
        'investing-in-emerging-technologies-answer': 'Investing in Emerging Technologies',
        'monitoring-competitor-strategies-answer': 'Monitoring Competitor Strategies',
        'adapting-marketing-channels-answer': 'Adapting Marketing Channels',
        'collaborative-innovation-answer': 'Collaborative Innovation',
        'strategic-partnerships-answer': 'Strategic Partnerships',
        'employee-training-and-development-answer': 'Employee Training and Development'
    }),
    (answer_map_page_four_q5, {
        'advanced-data-analytics-answer': 'Advanced Data Analytics',
        'leveraging-AI-and-machine-learning-answer': 'Leveraging AI and Machine Learning',
        'using-predictive-analytics-answer': 'Using Predictive Analytics',
        'market-research-and-surveys-answer': 'Market Research and Surveys',
        'monitoring-industry-reports-answer': 'Monitoring Industry Reports',
        'customer-feedback-and-behavior-analysis-answer': 'Customer Feedback and Behavior Analysis',
        'competitive-analysis-answer': 'Competitive Analysis',
        'trend-monitoring-tools-answer': 'Trend Monitoring Tools',
        'engaging-with-thought-leaders-answer': 'Engaging with Thought Leaders',
        'collaborating-with-tech-partners-answer': 'Collaborating with Tech Partners'
    }),
    (answer_map_page_four_q6, {
        'investing-in-emerging-technologies-q6-answer': 'Investing in Emerging Technologies',
        'continuous-learning-and-development-answer': 'Continuous Learning and Development',
        'agile-and-flexible-approach-answer': 'Agile and Flexible Approach',
        'customer-centric-focus-answer': 'Customer-Centric Focus',
        'strategic-partnerships-answer': 'Strategic Partnerships',
        'innovation-culture-answer': 'Innovation Culture',
        'regular-market-analysis-answer': 'Regular Market Analysis',
        'upskilling-and-reskilling-answer': 'Upskilling and Reskilling',
        'cybersecurity-measures-answer': 'Cybersecurity Measures',
        'adopting-best-practices-answer': 'Adopting Best Practices'
    }),
    (answer_map_page_four_q7, {
        'data-driven-insights-answer': 'Data-Driven Insights',
        'personalization-and-customer-experience-answer': 'Personalization and Customer Experience',
        'adapting-to-technological-advancements-answer': 'Adapting to Technological Advancements',
        'content-strategy-optimization-answer': 'Content Strategy Optimization',
        'social-media-engagement-answer': 'Social Media Engagement',
        'seo-and-sem-strategies-answer': 'SEO and SEM Strategies',
        'competitive-analysis-answer': 'Competitive Analysis',
        'customer-feedback-and-surveys-answer': 'Customer Feedback and Surveys',
        'influencer-and-partnership-collaborations-answer': 'Influencer and Partnership Collaborations',
        'agile-marketing-approach-answer': 'Agile Marketing Approach'
    }),
    (answer_map_page_four_q8, {
        'continuous-market-research-answer': 'Continuous Market Research',
        'customer-feedback-and-surveys-answer': 'Customer Feedback and Surveys',
        'competitive-analysis-answer': 'Competitive Analysis',
        'trend-analysis-tools-answer': 'Trend Analysis Tools',
        'industry-reports-and-publications-answer': 'Industry Reports and Publications',
        'collaborations-and-partnerships-answer': 'Collaborations and Partnerships'
    }),
    (answer_map_page_four_q9, {
        'personalized-customer-interactions-answer': 'Personalized Customer Interactions',
        'omnichannel-integration-answer': 'Omnichannel Integration',
        'adopting-AI-powered-support-answer': 'Adopting AI-Powered Support',
        'voice-of-customer-programs-answer': 'Voice of Customer (VoC) Programs',
        'proactive-customer-support-answer': 'Proactive Customer Support',
        'enhanced-data-privacy-and-security-answer': 'Enhanced Data Privacy and Security'
    }),
    (answer_map_page_four_q10, {
        'identifying-emerging-markets-answer': 'Identifying Emerging Markets',
        'sales-forecasting-answer': 'Sales Forecasting',
        'adjusting-sales-tactics-answer': 'Adjusting Sales Tactics',
        'product-positioning-and-messaging-answer': 'Product Positioning and Messaging',
        'customer-segmentation-answer': 'Customer Segmentation',
        'competitive-benchmarking-answer': 'Competitive Benchmarking'
    })
])

def test_page_four_positive_mappings(mapping, expected_pairs):

    # Verify that each key-value pair exists in the mapping
    for key, value in expected_pairs.items():
        assert key in mapping, f"Key {key} is missing from the mapping."
        assert mapping[key] == value, f"Value for key {key} is incorrect. Expected {value}, got {mapping[key]}."

    # Verify that all expected values are present
    for value in expected_pairs.values():
        assert value in mapping.values(), f"Expected value {value} is missing from the mapping."


@pytest.mark.parametrize("mapping,unexpected_keys,unexpected_values", [
    (answer_map_page_four_q1,
     ['invalid-key-1', 'fake-key'], 
     ['Invalid Value 1', 'Fake Value']),
    (answer_map_page_four_q2,
     ['unknown-key', 'unmapped-key'], 
     ['Unknown Value', 'Unmapped Value']),
    (answer_map_page_four_q3,
     ['wrong-key', 'dummy-key'], 
     ['Wrong Value', 'Dummy Value']),
    (answer_map_page_four_q4,
     ['error-key', 'nonexistent-key'], 
     ['Error Value', 'Nonexistent Value']),
    (answer_map_page_four_q5,
     ['placeholder-key', 'example-key'], 
     ['Placeholder Value', 'Example Value']),
    (answer_map_page_four_q6,
     ['bogus-key', 'nonsense-key'], 
     ['Bogus Value', 'Nonsense Value']),
    (answer_map_page_four_q7,
     ['irrelevant-key', 'unused-key'], 
     ['Irrelevant Value', 'Unused Value']),
    (answer_map_page_four_q8,
     ['test-key', 'invalid-entry'], 
     ['Test Value', 'Invalid Entry']),
    (answer_map_page_four_q9,
     ['nonexistent-id', 'invalid-key'], 
     ['Nonexistent Value', 'Invalid Key']),
    (answer_map_page_four_q10,
     ['missing-key', 'fake-id'], 
     ['Missing Value', 'Fake ID']),
])
def test_page_four_negative_mappings(mapping, unexpected_keys, unexpected_values):

    # Ensure unexpected keys are NOT in the mapping
    for key in unexpected_keys:
        assert key not in mapping, f"Unexpected key {key} found in the mapping."

    # Ensure unexpected values are NOT in the mapping
    for value in unexpected_values:
        assert value not in mapping.values(), f"Unexpected value {value} found in the mapping."
