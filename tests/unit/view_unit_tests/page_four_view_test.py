import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_four_structure(client):
    """Test the overall structure and metadata of Page Four: PageFourMarketTrends."""
    response = client.get('/PageFourMarketTrends')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Page Four: Market Trends'

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
        '/static/content/home-page.css',
        '/static/content/page-one.css'
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
    assert h1_tag.string == 'Market Trends'

def test_page_four_navigation_buttons(client):
    """Test the navigation buttons on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check navigation buttons using the `string` argument
    submit_button = soup.find('button', type='submit')
    assert submit_button is not None

    back_button = soup.find('button', string='Back')
    assert back_button is not None
    assert back_button['onclick'] == "history.back();"

    next_button = soup.find('button', string='Next')
    assert next_button is not None
    assert next_button['onclick'] == "window.location='/PageFiveDigitalMarketing';"


def test_page_four_question_one(client):
    """Test Question One (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-one')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'market-research-and-analysis-answer',
        'customer-feedback-and-insights-answer',
        'networking-and-conferences-answer',
        'professional-organizations-answer',
        'regular-industry-reading-answer',
        'social-media-monitoring-answer',
        'technology-tools-and-alerts-answer',
        'internal-knowledge-sharing-answer',
        'online-courses-and-certifications-answer',
        'mentorship-and-collaboration-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_two(client):
    """Test Question Two (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-two')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 8 # There are 8 checkboxes in the HMTL for Question One

        # Validate checkbox values
    expected_checkbox_values = [
        'data-driven-decision-making-answer',
        'enhanced-customer-experience-answer',
        'agility-and-adaptability-answer',
        'innovation-and-competitive-edge-answer',
        'accelerated-digital-transformation-answer',
        'operational-efficiency-answer',
        'employee-empowerment-answer',
        'sustainability-initiatives-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_three(client):
    """Test Question Four (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-three')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

        # Validate checkbox values
    expected_checkbox_values = [
        'adopting-AI-and-machine-learning-answer',
        'investing-in-data-analytics-answer',
        'enhancing-cybersecurity-measures-answer',
        'embracing-cloud-computing-answer',
        'developing-digital-products-and-services-answer',
        'implementing-IoT-solutions-answer',
        'collaborating-with-tech-partners-answer',
        'fostering-a-culture-of-innovation-answer',
        'exploring-blockchain-technology-answer',
        'sustainability-through-digital-solutions-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_four(client):
    """Test Question Four (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-four')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

        # Validate checkbox values
    expected_checkbox_values = [
        'leveraging-data-and-analytics-answer',
        'continuous-market-analysis-answer',
        'customer-feedback-integration-answer',
        'agile-methodologies-answer',
        'investing-in-emerging-technologies-answer',
        'monitoring-competitor-strategies-answer',
        'adapting-marketing-channels-answer',
        'collaborative-innovation-answer',
        'strategic-partnerships-answer',
        'employee-training-and-development-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_five(client):
    """Test Question Five (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-five')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'advanced-data-analytics-answer',
        'leveraging-AI-and-machine-learning-answer',
        'using-predictive-analytics-answer',
        'market-research-and-surveys-answer',
        'monitoring-industry-reports-answer',
        'customer-feedback-and-behavior-analysis-answer',
        'competitive-analysis-answer',
        'trend-monitoring-tools-answer',
        'engaging-with-thought-leaders-answer',
        'collaborating-with-tech-partners-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_six(client):
    """Test Question Six (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-six')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'investing-in-emerging-technologies-answer',
        'continuous-learning-and-development-answer',
        'agile-and-flexible-approach-answer',
        'customer-centric-focus-answer',
        'strategic-partnerships-answer',
        'innovation-culture-answer',
        'regular-market-analysis-answer',
        'upskilling-and-reskilling-answer',
        'cybersecurity-measures-answer',
        'adopting-best-practices-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_four_question_seven(client):
    """Test Question Seven (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-seven')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'data-driven-insights-answer',
        'personalization-and-customer-experience-answer',
        'adapting-to-technological-advancements-answer',
        'content-strategy-optimization-answer',
        'social-media-engagement-answer',
        'seo-and-sem-strategies-answer',
        'competitive-analysis-answer',
        'customer-feedback-and-surveys-answer',
        'influencer-and-partnership-collaborations-answer',
        'agile-marketing-approach-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_eight(client):
    """Test Question Eight (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-eight')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'continuous-market-research-answer',
        'customer-feedback-and-surveys-answer',
        'competitive-analysis-answer',
        'trend-analysis-tools-answer',
        'industry-reports-and-publications-answer',
        'collaborations-and-partnerships-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_nine(client):
    """Test Question Nine (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-nine')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'personalized-customer-interactions-answer',
        'omnichannel-integration-answer',
        'adopting-AI-powered-support-answer',
        'voice-of-customer-programs-answer',
        'proactive-customer-support-answer',
        'enhanced-data-privacy-and-security-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_four_question_ten(client):
    """Test Question Ten (checkboxes) on Page Four: Market Trends."""
    response = client.get('/PageFourMarketTrends')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-four-question-ten')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6 # There are 10 checkboxes in the HMTL for Question One

    # Validate checkbox values
    expected_checkbox_values = [
        'identifying-emerging-markets-answer',
        'sales-forecasting-answer',
        'adjusting-sales-tactics-answer',
        'product-positioning-and-messaging-answer',
        'customer-segmentation-answer',
        'competitive-benchmarking-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values