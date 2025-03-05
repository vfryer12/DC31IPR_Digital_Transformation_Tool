import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_five_structure(client):

    response = client.get('/PageFiveDigitalMarketing')
    response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Page Five: Digital Marketing'

    # Check meta tags
    meta_charset = soup.find('meta', attrs={'charset': 'UTF-8'})
    meta_viewport = soup.find('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'})
    meta_compat = soup.find('meta', attrs={'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'})
    assert meta_charset is not None
    assert meta_viewport is not None
    assert meta_compat is not None

    # Check stylesheets
    stylesheets = soup.find_all('link', rel='stylesheet')
    expected_stylesheets = [
        '/static/content/standard-page.css'
    ]
    hrefs=[link['href'] for link in stylesheets]
    for stylesheet in expected_stylesheets:
        assert stylesheet in hrefs

    # Check scrips
    scripts = soup.find_all('script', type='module')
    expected_stylesheets = [
        '\\static\\PageOne.js',
        '\\static\\FetchAssessmentHeader.js',
        '\\static\\FetchAssessmentFooter.js'
    ]
    srcs = [script['src'] for script in scripts]
    for script in expected_stylesheets:
        assert script in srcs

    # Check header
    header = soup.find('div', {'id': 'header-placeholder'})
    assert header is not None

    # Check footer
    footer = soup.find('div', {'id': 'footer-placeholder'})
    assert footer is not None

    # Check for presence of h1 tag directly in the main content
    main_content = soup.find('div', {'class': 'main'})
    assert main_content is not None
    h1_tag = main_content.find('h1')
    assert h1_tag is not None
    assert h1_tag.string == 'Digital Marketing'

def test_page_four_navigation_buttons(client):
    """Test the navigation buttons on Page Five: Digital Marketing."""
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check navigation buttons using the `string` argument
    submit_button = soup.find('button', type='submit')
    assert submit_button is not None

    back_button = soup.find('button', string='Back')
    assert back_button is not None
    assert back_button['onclick'] == "history.back();"

    next_button = soup.find('button', string='Next')
    assert next_button is not None
    assert next_button['onclick'] == "window.location='/SubmitAssessmentPage';"

def test_page_five_question_one(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-one')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'search-engine-optimization-answer',
        'social-media-marketing-answer',
        'content-marketing-answer',
        'pay-per-click-advertising-answer',
        'email-marketing-answer',
        'influencer-marketing-answer',
        'video-marketing-answer',
        'retargeting-campaigns-answer',
        'affiliate-marketing-answer',
        'webinars-and-live-streams-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_two(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-two')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'return-on-investment-answer',
        'conversion-rate-answer',
        'customer-acquisition-cost-answer',
        'customer-lifetime-value-answer',
        'website-traffic-answer',
        'lead-generation-answer',
        'engagement-metrics-answer',
        'social-media-metrics-answer',
        'email-open-and-click-through-rates-answer',
        'bounce-rate-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_three(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-three')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'utilizing-data-analytics-answer',
        'enhancing-seo-practices-answer',
        'expanding-social-media-presence-answer',
        'investing-in-content-marketing-answer',
        'improving-email-marketing-campaigns-answer',
        'implementing-marketing-automation-answer',
        'leveraging-influencer-partnerships-answer',
        'expanding-video-marketing-answer',
        'optimizing-mobile-marketing-answer',
        'focusing-on-customer-experience-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_four(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-four')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'defining-goals-and-key-performance-indicators-answer',
        'analyzing-and-interpreting-data-answer',
        'personalizing-marketing-campaigns-answer',
        'predictive-analytics-answer',
        'optimizing-marketing-channels-answer',
        'real-time-analytics-answer',
        'a/b-testing-answer',
        'customer-journey-mapping-answer',
        'collecting-and-cleansing-data-answer',
        'reporting-and-visualization-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_five_question_five(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-five')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'keyword-research-answer',
        'on-page-optimization-answer',
        'content-creation-answer',
        'technical-seo-answer',
        'link-building-answer',
        'user-experience-optimization-answer',
        'local-seo-answer',
        'regular-audits-and-updates-answer',
        'analytics-and-reporting-answer',
        'competitor-analysis-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_six(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-six')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'building-brand-awareness-answer',
        'engaging-with-customers-answer',
        'running-paid-advertising-campaigns-answer',
        'content-promotion-answer',
        'providing-customer-support-answer',
        'influencer-collaborations-answer',
        'social-listening-answer',
        'analyzing-performance-metrics-answer',
        'hosting-contests-and-giveaways-answer',
        'creating-a-content-calendar-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_seven(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-seven')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'personalized-campaigns-answer',
        'automated-email-sequences-answer',
        'promotional-emails-answer',
        'abandoned-cart-emails-answer',
        'newsletters-answer',
        'transactional-emails-answer',
        're-engagement-campaigns-answer',
        'event-invitations-answer',
        'surveys-and-feedback-requests-answer',
        'educational-content-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_eight(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-eight')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'creating-valuable-blog-content-answer',
        'seo-optimization-answer',
        'developing-video-content-answer',
        'utilizing-social-media-answer',
        'publishing-ebooks-and-whitepapers-answer',
        'hosting-webinars-and-live-events-answer',
        'email-newsletters-answer',
        'creating-infographics-answer',
        'podcasting-answer',
        'user-generated-content-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_nine(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-nine')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'partnering-with-relevant-influencers-answer',
        'creating-authentic-content-answer',
        'leveraging-micro-influencers-answer',
        'tracking-and-analyzing-performance-answer',
        'building-long-term-relationships-answer',
        'utilizing-influencer-reviews-and-testimonials-answer',
        'creating-sponsored-content-answer',
        'hosting-giveaways-and-contests-answer',
        'running-influencer-takeovers-answer',
        'utilizing-influencer-content-across-channels-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_five_question_ten(client):
    response = client.get('/PageFiveDigitalMarketing')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-five-question-ten')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'product-demonstrations-answer',
        'customer-testimonials-answer',
        'educational-content-answer',
        'video-ads-answer',
        'social-media-videos-answer',
        'live-streaming-answer',
        'explainer-videos-answer',
        'behind-the-scenes-footage-answer',
        'user-generated-content-answer',
        'interactive-videos-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values
