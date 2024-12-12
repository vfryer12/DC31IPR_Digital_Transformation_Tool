import pytest

# Import the mappings
from controllers.utils.mappings_page_one import (
    answer_map_q1,
    answer_map_q2,
    answer_map_q3,
    answer_map_q4,
    answer_map_q5,
    answer_map_q6,
    answer_map_q7,
    answer_map_q8,
    answer_map_q9,
    answer_map_q10
)

@pytest.mark.parametrize("mapping,expected_pairs", [
    (answer_map_q1, {
        '1': 'No plan in place',
        '2': 'Needs Improvement',
        '3': 'Fully Aligned'
    }),
    (answer_map_q2, {
        'cio': 'Chief Information Officer (CIO)',
        'cto': 'Chief Technology Officer (CTO)',
        'dtm': 'Digital Transformation Manager',
        'cdo': 'Chief Digital Officer (CDO)',
        'itd': 'IT Director/Manager',
        'bul': 'Business Unit Leader',
        'md': 'Marketing Director',
        'dal': 'Data Analytics Leader',
        'other': 'Other'
    }),
    (answer_map_q3, {
        'never': 'Never',
        'monthly': 'Every Month',
        'quarterly': 'Quarterly',
        'year': 'Annual',
        'continuous': 'Continuous'
    }),
    (answer_map_q4, {
        'return-on-investment-answer': 'Return on Investment (ROI)',
        'conversion-rates-answer': 'Conversion Rates',
        'customer-acquisition-cost-and-customer-lifetime-value-answer': 'Customer Acquisition Cost (CAC) and Customer Lifetime Value (CLV)',
        'website-traffic-answer': 'Website Traffic',
        'customer-engagement-answer': 'Customer Engagement',
        'social-media-metrics-and-email-marketing-metrics-answer': 'Social Media Metrics and Email Marketing Metrics',
        'seo-rankings-answer': 'SEO Rankings'
    }),
    (answer_map_q5, {
        'csat-metrics-answer': 'Customer Satisfaction Score (CSAT)',
        'ces-metrics-answer': 'Customer Effort Service (CES)',
        'digital-investments-answer': 'Return on Digiital Investments',
        'employee-productivity-answer': 'Employee Productivity',
        'adoption-performance-answer': 'Adoption & Performance Metrics',
        'customer-experience-metrics': 'Customer Experience Metrics',
        'percentage-ai-business-answer': 'Percentage of AI-Enabled Businesses',
        'reliability-availability-answer': 'Reliability & Availability',
        'cost-benefit-answer': 'Cost-Benefit Analysis',
        'revenue-digital-tech-answer': 'Revenue from Digital Technology',
        'percent-cloud-deploy-answer': 'Percentage of Cloud Deployments',
        'active-usage-metric-answer': 'Active Usage Metrics',
        'conversion-rate-answer': 'Conversion Rate',
        'customer-value-answer': 'Customer Lifetime Value',
        'website-traffic-answer': 'Website Traffic',
        'social-engagement-answer': 'Social Media Engagement',
        'brand-engagement-answer': 'Brand Engagement On Website',
        'traffic-sources-answer': 'Traffic Sources',
        'landing-page-answer': 'Landing Page Conversions',
        'inbound-marketing-answer': 'Inbound Marketing ROI',
        'social-traffic-answer': 'Social Media Traffic'
    }),
    (answer_map_q6, {
        'clear-communication-answer': 'Clear Communication',
        'engagement-answer': 'Engagement',
        'training-answer': 'Training',
        'feedback-answer': 'Feedback',
        'leadership-answer': 'Leadership',
        'incentives-answer': 'Incentives',
        'monitoring-answer': 'Monitoring'
    }),
    (answer_map_q7, {
        'alignment-answer': 'Alignment',
        'resistance-to-change-answer': 'Resistance to Change',
        'skill-gaps-answer': 'Skill Gaps',
        'resource-allocation-answer': 'Resource Allocation',
        'data-management-answer': 'Data Management',
        'keeping-pace-answer': 'Keeping Pace',
        'measuring-success-answer': 'Measuring Success'
    }),
    (answer_map_q8, {
        'feedback-mechanisms-answer': 'Feedback Mechanisms',
        'data-analysis-answer': 'Data Analysis',
        'regular-reviews-answer': 'Regular Reviews',
        'adaptability-answer': 'Adaptability',
        'communication-answer': 'Communication',
        'documentation-answer': 'Documentation'
    }),
    (answer_map_q9, {
        'strategic-fit-answer': 'Strategic Fit',
        'research-answer': 'Research',
        'risk-assessment-answer': 'Risk Assessment',
        'pilot-projects-answer': 'Pilot Projects',
        'training-answer': 'Training',
        'scalability-answer': 'Scalability'
    }),
    (answer_map_q10, {
        'understanding-needs-answer': 'Understanding Needs',
        'personalization-answer': 'Personalization',
        'seamless-experience-answer': 'Seamless Experience',
        'customer-feedback-answer': 'Customer Feedback',
        'engagement-answer': 'Engagement',
        'measurement-answer': 'Measurement'
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
    (answer_map_q1,
     ['invalid-key-1', 'fake-key'], 
     ['Invalid Value 1', 'Fake Value']),
    (answer_map_q2,
     ['unknown-key', 'unmapped-key'], 
     ['Unknown Value', 'Unmapped Value']),
    (answer_map_q3,
     ['wrong-key', 'dummy-key'], 
     ['Wrong Value', 'Dummy Value']),
    (answer_map_q4,
     ['error-key', 'nonexistent-key'], 
     ['Error Value', 'Nonexistent Value']),
    (answer_map_q5,
     ['placeholder-key', 'example-key'], 
     ['Placeholder Value', 'Example Value']),
    (answer_map_q6,
     ['bogus-key', 'nonsense-key'], 
     ['Bogus Value', 'Nonsense Value']),
    (answer_map_q7,
     ['irrelevant-key', 'unused-key'], 
     ['Irrelevant Value', 'Unused Value']),
    (answer_map_q8,
     ['test-key', 'invalid-entry'], 
     ['Test Value', 'Invalid Entry']),
    (answer_map_q9,
     ['nonexistent-id', 'invalid-key'], 
     ['Nonexistent Value', 'Invalid Key']),
    (answer_map_q10,
     ['missing-key', 'fake-id'], 
     ['Missing Value', 'Fake ID']),
])
def test_page_one_negative_mappings(mapping, unexpected_keys, unexpected_values):
    """
    Negative tests to ensure mappings do not include unexpected keys or values.
    """
    # Ensure unexpected keys are NOT in the mapping
    for key in unexpected_keys:
        assert key not in mapping, f"Unexpected key {key} found in the mapping."

    # Ensure unexpected values are NOT in the mapping
    for value in unexpected_values:
        assert value not in mapping.values(), f"Unexpected value {value} found in the mapping."

