import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_two_struture(client):
    response = client.get('/PageTwoDigitalSkills')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Page Two: Digital Skills'

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
    hrefs =[link['href'] for link in stylesheets]
    for stylesheet in expected_stylesheets:
        assert stylesheet in hrefs

    # Check scripts
    scripts = soup.find_all('script', type='module')
    expected_scripts = [
        '\\static\\PageFunctionality.js',
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
    assert h1_tag.string == 'Digital Strategy'

def test_page_two_navigation_buttons(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check navigation buttons using the string argument
    submit_button = soup.find('button', type='submit')
    assert submit_button is not None

    back_button = soup.find('button', string='Back')
    assert back_button is not None
    assert back_button['onclick'] == "history.back();"

    next_button = soup.find('button', string='Next')
    assert next_button is not None
    assert next_button['onclick'] == "window.location='/PageThreeTechnologyAdoption';"


def test_page_two_question_one(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-one')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'data-analysis-answer',
        'cybersecurity-answer',
        'cloud-computing-answer',
        'artificial-intelligence-and-machine-learning-answer',
        'software-development-answer',
        'project-management-answer',
        'digital-marketing-answer',
        'ux/ui-design-answer',
        'remote-collaboration-tools-answer',
        'blockchain-technology-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_two(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-two')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 7

    # Validate checkbox values
    expected_checkbox_values = [
        'skill-specific-tests-answer',
        'certifications-and-qualifications-answer',
        'practical-exercises-answer',
        'behavioral-interview-questions-answer',
        'online-assessments-answer',
        'peer-review-answer',
        'hiring-via-recruiter-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_three(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-three')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10 

    # Validate checkbox values
    expected_checkbox_values = [
        'training-programs-answer',
        'online-learning-platforms-answer',
        'workshops-and-seminars-answer',
        'learning-and-development-budget-answer',
        'mentorship-programs-answer',
        'project-based-learning-answer',
        'encourage-self-learning-answer',
        'regular-assessments-and-feedback-answer',
        'recognize-and-reward-learning-answer',
        'stay-updated-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_four(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-four')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'leadership-support-answer',
        'promote-a-growth-mindset-answer',
        'provide-learning-resources-answer',
        'learning-and-development-programs-answer',
        'encourage-self-learning-answer',
        'regular-skill-assessments-answer',
        'feedback-culture-answer',
        'recognize-and-reward-learning-answer',
        'create-learning-communities-answer',
        'stay-updated-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_five(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-five')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 10

    # Validate checkbox values
    expected_checkbox_values = [
        'data-analysis-q5-answer',
        'cybersecurity-q5-answer',
        'cloud-computing-q5-answer',
        'artificial-intelligence-and-machine-learning-answer',
        'software-development-answer',
        'digital-marketing-answer',
        'ux/ui-design-answer',
        'project-management-answer',
        'remote-collaboration-answer',
        'blockchain-technology-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_six(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-six')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6

    # Validate checkbox values
    expected_checkbox_values = [
        'training-and-development-programs-answer',
        'hiring-new-talent-answer',
        'encouraging-continuous-learning-answer',
        'leveraging-technology-answer',
        'partnerships-with-educational-institutions-answer',
        'outsourcing-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_seven(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-seven')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6

    # Validate checkbox values
    expected_checkbox_values = [
        'continuous-learning-answer',
        'networking-answer',
        'following-industry-news-answer',
        'hands-on-practice-answer',
        'mentorship-answer',
        'certifications-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_eight(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-eight')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6

    # Validate checkbox values
    expected_checkbox_values = [
        'skills-assessment-answer',
        'training-and-development-q8-answer',
        'hiring-strategy-answer',
        'encourage-continuous-learning-answer',
        'leverage-technology-answer',
        'partnerships-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_nine(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-nine')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 6

    # Validate checkbox values
    expected_checkbox_values = [
        'training-and-development-answer',
        'support-and-resources-answer',
        'culture-of-adaptability-answer',
        'pilot-testing-answer',
        'feedback-mechanisms-answer',
        'leadership-involvement-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values

def test_page_two_question_ten(client):
    response = client.get('/PageTwoDigitalSkills')
    soup = BeautifulSoup(response.data, 'html.parser')

    question_one_div = soup.find('div', id='page-two-question-ten')
    assert question_one_div is not None

    checkboxes = question_one_div.find_all('input', type='checkbox')
    assert len(checkboxes) == 7

    # Validate checkbox values
    expected_checkbox_values = [
        'competitive-compensation-answer',
        'career-development-opportunities-answer',
        'continuous-learning-and-development-answer',
        'workplace-culture-answer',
        'flexible-work-arrangements-answer',
        'interesting-projects-answer',
        'employer-branding-answer'
    ]
    actual_checkbox_values = [checkbox['value'] for checkbox in checkboxes]
    for value in expected_checkbox_values:
        assert value in actual_checkbox_values