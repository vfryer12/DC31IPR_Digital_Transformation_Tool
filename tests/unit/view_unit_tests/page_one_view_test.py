import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_one_structure(client):
    """Test the overall structure and metadata of Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Page One: Digital Strategy'

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
    hrefs = [link['href'] for link in stylesheets]
    for stylesheet in expected_stylesheets:
        assert stylesheet in hrefs

    # Check scripts
    scripts = soup.find_all('script', type='module')
    expected_scripts = [
        '\\static\\PageOne.js',
        '\\static\\FetchAssessmentHeader.js',
        '\\static\\FetchAssessmentFooter.js'
    ]
    srcs = [script['src'] for script in scripts]
    for script in expected_scripts:
        assert script in srcs

def test_page_one_navigation_buttons(client):
    """Test the navigation buttons on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check navigation buttons using the `string` argument
    back_button = soup.find('button', string='Back')
    next_button = soup.find('button', string='Next')
    submit_button = soup.find('button', type='submit')
    assert back_button is not None
    assert next_button is not None
    assert submit_button is not None

def test_page_one_question_one(client):
    """Test Question One (radio buttons) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='question-one')
    assert question_one_div is not None
    radio_buttons = question_one_div.find_all('input', type='radio')
    assert len(radio_buttons) == 3
    radio_values = [radio['value'] for radio in radio_buttons]
    assert '1' in radio_values
    assert '2' in radio_values
    assert '3' in radio_values

def test_page_one_question_two(client):
    """Test Question Two (dropdown) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_two_div = soup.find('div', id='question-two')
    assert question_two_div is not None
    dropdown = question_two_div.find('select', id='question-two-dropdown')
    assert dropdown is not None
    dropdown_options = dropdown.find_all('option')
    option_values = [option['value'] for option in dropdown_options if 'value' in option.attrs]
    expected_options = [
        '', 'cio', 'cto', 'dtm', 'cdo', 'itd', 'bul', 'md', 'dal', 'other'
    ]
    for value in expected_options:
        assert value in option_values

def test_page_one_question_three(client):
    """Test Question Three (radio buttons) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='question-three')
    assert question_one_div is not None
    radio_buttons = question_one_div.find_all('input', type='radio')
    assert len(radio_buttons) == 5
    radio_values = [radio['value'] for radio in radio_buttons]
    assert 'never' in radio_values
    assert 'monthly' in radio_values
    assert 'quarterly' in radio_values
    assert 'year' in radio_values
    assert 'continuous' in radio_values

def test_page_one_question_four(client):
    """Test Question Four (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-four')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 7  # There are 7 checkboxes in the HTML for Question Four

    # Validate checkbox values
    expected_checkbox_values = [
        'return-on-investment-answer',
        'conversion-rates-answer',
        'customer-acquisition-cost-and-customer-lifetime-value-answer',
        'website-traffic-answer',
        'customer-engagement-answer',
        'social-media-metrics-and-email-marketing-metrics-answer',
        'seo-rankings-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_one_question_five(client):
    """Test Question Five (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-five')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 21  # There are 21 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'csat-metrics-answer',
        'ces-metrics-answer',
        'digital-investments-answer',
        'employee-productivity-answer',
        'adoption-performance-answer',
        'customer-experience-metrics',
        'percentage-ai-business-answer',
        'reliability-availability-answer',
        'cost-benefit-answer',
        'revenue-digital-tech-answer',
        'percent-cloud-deploy-answer',
        'active-usage-metric-answer',
        'conversion-rate-answer',
        'customer-value-answer',
        'website-traffic-answer',
        'social-engagement-answer',
        'brand-engagement-answer',
        'traffic-sources-answer',
        'landing-page-answer',
        'inbound-marketing-answer',
        'social-traffic-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_one_question_six(client):
    """Test Question Six (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-six')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 7  # There are 7 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'clear-communication-answer',
        'engagement-answer',
        'training-answer',
        'feedback-answer',
        'leadership-answer',
        'incentives-answer',
        'monitoring-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_one_question_seven(client):
    """Test Question Seven (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-seven')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 7  # There are 7 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'alignment-answer',
        'resistance-to-change-answer',
        'skill-gaps-answer',
        'resource-allocation-answer',
        'data-management-answer',
        'keeping-pace-answer',
        'measuring-success-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_one_question_eight(client):
    """Test Question Eight (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-eight')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6  # There are 6 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'feedback-mechanisms-answer',
        'data-analysis-answer',
        'regular-reviews-answer',
        'adaptability-answer',
        'communication-answer',
        'documentation-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_one_question_nine(client):
    """Test Question Nine (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-nine')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6  # There are 6 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'strategic-fit-answer',
        'research-answer',
        'risk-assessment-answer',
        'pilot-projects-answer',
        'training-answer',
        'scalability-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_one_question_ten(client):
    """Test Question Ten (checkboxes) on Page One: Digital Strategy."""
    response = client.get('/PageOneDigitalStrategy')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_four_div = soup.find('div', id='question-ten')
    assert question_four_div is not None

    checkboxes = question_four_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6  # There are 6 checkboxes in the HTML for Question Five

    # Validate checkbox values
    expected_checkbox_values = [
        'understanding-needs-answer',
        'personalization-answer',
        'seamless-experience-answer',
        'customer-feedback-answer',
        'engagement-answer',
        'measurement-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values