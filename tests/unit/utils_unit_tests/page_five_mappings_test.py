import pytest

# Sample mappings for testing
from controllers.utils.mappings_page_five import (
    answer_map_page_five_q1,
    answer_map_page_five_q2,
    answer_map_page_five_q3,
    answer_map_page_five_q4,
    answer_map_page_five_q5,
    answer_map_page_five_q6,
    answer_map_page_five_q7,
    answer_map_page_five_q8,
    answer_map_page_five_q9,
    answer_map_page_five_q10,
)

@pytest.mark.parametrize("mapping,expected_keys,expected_values", [
    (answer_map_page_five_q1, 
     ['search-engine-optimization-answer', 'social-media-marketing-answer', 'content-marketing-answer'], 
     ['Search Engine Optimization (SEO)', 'Social Media Marketing', 'Content Marketing']),
    (answer_map_page_five_q2, 
     ['return-on-investment-answer', 'conversion-rate-answer', 'customer-acquisition-cost-answer'], 
     ['Return on Investment (ROI)', 'Conversion Rate', 'Customer Acquisition Cost (CAC)']),
    (answer_map_page_five_q3, 
     ['utilizing-data-analytics-answer', 'enhancing-seo-practices-answer', 'expanding-social-media-presence-answer'], 
     ['Utilizing Data Analytics', 'Enhancing SEO Practices', 'Expanding Social Media Presence']),
    (answer_map_page_five_q4, 
     ['defining-goals-and-key-performance-indicators-answer', 'analyzing-and-interpreting-data-answer', 'personalizing-marketing-campaigns-answer'], 
     ['Defining Goals and Key Performance Indicators (KPIs)', 'Analyzing and Interpreting Data', 'Personalizing Marketing Campaigns']),
    (answer_map_page_five_q5, 
     ['keyword-research-answer', 'on-page-optimization-answer', 'content-creation-answer'], 
     ['Keyword Research', 'On-Page Optimization', 'Content Creation']),
    (answer_map_page_five_q6, 
     ['building-brand-awareness-answer', 'engaging-with-customers-answer', 'running-paid-advertising-campaigns-answer'], 
     ['Building Brand Awareness', 'Engaging with Customers', 'Running Paid Advertising Campaigns']),
    (answer_map_page_five_q7, 
     ['personalized-campaigns-answer', 'automated-email-sequences-answer', 'promotional-emails-answer'], 
     ['Personalized Campaigns', 'Automated Email Sequences', 'Promotional Emails']),
    (answer_map_page_five_q8, 
     ['creating-valuable-blog-content-answer', 'seo-optimization-answer', 'developing-video-content-answer'], 
     ['Creating Valuable Blog Content', 'SEO Optimization', 'Developing Video Content']),
    (answer_map_page_five_q9, 
     ['partnering-with-relevant-influencers-answer', 'creating-authentic-content-answer', 'leveraging-micro-influencers-answer'], 
     ['Partnering with Relevant Influencers', 'Creating Authentic Content', 'Leveraging Micro-Influencers']),
    (answer_map_page_five_q10, 
     ['product-demonstrations-answer', 'customer-testimonials-answer', 'educational-content-answer'], 
     ['Product Demonstrations', 'Customer Testimonials', 'Educational Content']),
])

def test_page_five_mappings(mapping, expected_keys, expected_values):
    """
    Test mappings for Page Five questions to ensure expected keys and values are present.
    """
    # Check that all expected keys are in the mapping
    for key in expected_keys:
        assert key in mapping, f"Key {key} is missing in the mapping."

    # Check that all expected values are in the mapping
    for value in expected_values:
        assert value in mapping.values(), f"Value {value} is missing in the mapping."

    # Ensure there are no duplicate keys or values
    assert len(mapping.keys()) == len(set(mapping.keys())), "Duplicate keys found in the mapping."
    assert len(mapping.values()) == len(set(mapping.values())), "Duplicate values found in the mapping."


@pytest.mark.parametrize("mapping,unexpected_keys,unexpected_values", [
    (answer_map_page_five_q1, 
     ['invalid-key-1', 'non-existent-key'], 
     ['Invalid Value 1', 'Non-existent Value']),
    (answer_map_page_five_q2, 
     ['irrelevant-key', 'unused-key'], 
     ['Irrelevant Value', 'Unused Value']),
    (answer_map_page_five_q3, 
     ['fake-key', 'wrong-key'], 
     ['Fake Value', 'Wrong Value']),
    (answer_map_page_five_q4, 
     ['bogus-key', 'false-key'], 
     ['Bogus Value', 'False Value']),
    (answer_map_page_five_q5, 
     ['placeholder-key', 'example-key'], 
     ['Placeholder Value', 'Example Value']),
    (answer_map_page_five_q6, 
     ['nonsense-key', 'test-key'], 
     ['Nonsense Value', 'Test Value']),
    (answer_map_page_five_q7, 
     ['error-key', 'key-xyz'], 
     ['Error Value', 'XYZ Value']),
    (answer_map_page_five_q8, 
     ['invalid-entry', 'not-a-key'], 
     ['Invalid Entry', 'Not a Key']),
    (answer_map_page_five_q9, 
     ['dummy-key', 'fake-id'], 
     ['Dummy Value', 'Fake ID']),
    (answer_map_page_five_q10, 
     ['wrong-answer', 'missing-key'], 
     ['Wrong Answer', 'Missing Key']),
])

def test_page_five_negative_mappings(mapping, unexpected_keys, unexpected_values):
    """
    Negative tests to ensure mappings do not include unexpected keys or values.
    """
    # Check that unexpected keys are NOT in the mapping
    for key in unexpected_keys:
        assert key not in mapping, f"Unexpected key {key} found in the mapping."

    # Check that unexpected values are NOT in the mapping
    for value in unexpected_values:
        assert value not in mapping.values(), f"Unexpected value {value} found in the mapping."
