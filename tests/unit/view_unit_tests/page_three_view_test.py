import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_three_structure(client):

    response = client.get('/PageThreeTechnologyAdoption')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Page Three: Technology Adoption'

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
    assert h1_tag.string == 'Technology Adoption'
    

def test_page_three_navigation_buttons(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check navigation buttons using the `string` argument
    submit_button = soup.find('button', type='submit')
    assert submit_button is not None

    back_button = soup.find('button', string='Back')
    assert back_button is not None
    assert back_button['onclick'] == "history.back();"

    next_button = soup.find('button', string='Next')
    assert next_button is not None
    assert next_button['onclick'] == "window.location='/PageFourMarketTrends';"

def test_page_three_question_one(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-one')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'define-clear-objectives-answer',
        'assess-alignment-with-your-business-answer',
        'feasibility-and-viability-check-answer',
        'risk-analysis-answer',
        'performance-against-KPIs-answer',
        'test-and-iterate-answer',
        'explore-market-potential-answer',
        'collaborate-and-seek-expert-input-answer',
        'user-friendliness-answer',
        'long-term-vision-assessmentg-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_two(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-two')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='radio')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'clear-communication-answer',
        'leadership-support-answer',
        'comprehensive-training-programs-answer',
        'change-management-strategies-answer',
        'user-friendly-design-answer',
        'support-systems-answer',
        'pilot-testing-answer',
        'gradual-implementation-answer',
        'feedback-mechanisms-answer',
        'monitor-and-evaluate-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_three(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-three')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'resistance-to-change-answer',
        'lack-of-skilled-personnel-answer',
        'complexity-of-technology-answer',
        'security-concerns-answer',
        'budget-constraints-answer',
        'inadequate-training-answer',
        'cultural-mindset-answer',
        'siloed-organizational-structure-answer',
        'continuous-evolution-of-customer-needs-answer',
        'measuring-ROI-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_four(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-four')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'user-adoption-rate-answer',
        'performance-metrics-answer',
        'return-on-investment-answer',
        'user-satisfaction-answer',
        'usage-frequency-answer',
        'business-impact-answer',
        'time-to-proficiency-answer',
        'support-requests-answer',
        'feature-adoption-rate-answer',
        'training-completion-rates-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_five(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-five')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'define-clear-business-goals-answer',
        'collaborate-with-stakeholders-answer',
        'conduct-a-needs-assessment-answer',
        'develop-a-unified-strategy-answer',
        'monitor-and-measure-performance-answer',
        'data-driven-decision-making-answer',
        'implement-governance-and-accountability-answer',
        'continuous-feedback-loops-answer',
        'encourage-cross-functional-collaboration-answer',
        'adapt-and-evolve-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_three_question_six(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-six')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'set-and-communicate-clear-goals-answer',
        'develop-a-comprehensive-strategy-answer',
        'provide-continuous-training-and-support-answer',
        'build-a-dedicated-change-management-team-answer',
        'plan-for-resistance-answer',
        'encourage-employee-involvement-answer',
        'monitor-and-evaluate-progress-answer',
        'communicate-regularly-answer',
        'foster-a-culture-of-innovationn-answer',
        'celebrate-successes-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_three_question_seven(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-seven')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'join-professional-organizations-answer',
        'attend-industry-conferences-and-tech-events-answer',
        'follow-tech-news-and-blogs-answer',
        'engage-on-social-media-answer',
        'take-online-courses-and-webinars-answer',
        'network-with-peers-answer',
        'find-a-mentor-answer',
        'watch-TED-talks-and-tech-videos-answer',
        'participate-in-online-forums-and-communities-answer',
        'read-industry-reports-and-whitepapers-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values


def test_page_three_question_eight(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-eight')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'regularly-review-and-update-answer',
        'stay-informed-on-industry-trends-answer',
        'implement-continuous-integration-and-deployment-answer',
        'conduct-regular-audits-answer',
        'engage-with-the-developer-community-answer',
        'foster-a-culture-of-learning-answer',
        'collaborate-with-vendors-and-partners-answer',
        'adopt-modular-architecture-answer',
        'monitor-and-analyze-performance-answer',
        'plan-for-scalability-and-future-growth-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_nine(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-nine')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'conduct-a-comprehensive-risk-assessment-answer',
        'develop-a-risk-mitigation-plan-answer',
        'perform-a-cost-benefit-analysis-answer',
        'conduct-cybersecurity-assessments-answer',
        'implement-pilot-testing-answer',
        'monitor-regulatory-compliance-answer',
        'engage-with-stakeholders-answer',
        'analyze-historical-data-answer',
        'use-risk-assessment-tools-answer',
        'seek-expert-consultation-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_three_question_ten(client):

    response = client.get('/PageThreeTechnologyAdoption')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-three-question-ten')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'communicate-the-benefits-answer',
        'involve-employees-early-answer',
        'provide-comprehensive-training-answer',
        'address-concerns-openly-answer',
        'implement-change-management-strategies-answer',
        'foster-a-positive-culture-answer',
        'provide-ongoing-support-answer',
        'showcase-success-stories-answer',
        'offer-incentive-answer',
        'monitor-and-adjust-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values