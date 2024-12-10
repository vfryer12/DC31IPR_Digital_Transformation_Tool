import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_submit_page_structure(client):
    """Test the overall structure and metadata of the Submit Page."""
    response = client.get('/SubmitAssessmentPage')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Submit Page'

    # Check meta tags
    meta_charset = soup.find('meta', attrs={'charset': 'UTF-8'})
    meta_viewport = soup.find('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'})
    meta_compat = soup.find('meta', attrs={'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'})
    assert meta_charset is not None
    assert meta_viewport is not None
    assert meta_compat is not None

    # Check stylesheets
    stylesheets = soup.find_all('link', rel='stylesheet')
    assert len(stylesheets) == 1
    assert stylesheets[0]['href'] == '/static/content/submit-page.css'

    # Check scripts
    scripts = soup.find_all('script', type='module')
    expected_scripts = [
        '\\static\\FetchAssessmentHeader.js',
        '\\static\\FetchAssessmentFooter.js',
    ]
    script_srcs = [script['src'] for script in scripts]
    for script in expected_scripts:
        assert script in script_srcs

    # Check header and footer placeholders
    header = soup.find('div', {'id': 'header-placeholder'})
    footer = soup.find('div', {'id': 'footer-placeholder'})
    assert header is not None
    assert footer is not None

def test_submit_page_content(client):
    """Test the content and form functionality on the Submit Page."""
    response = client.get('/SubmitAssessmentPage')
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check the main container
    container = soup.find('div', class_='container')
    assert container is not None

    # Check heading
    heading = container.find('h1')
    assert heading is not None
    assert heading.string == 'Thank You'

    # Check paragraph text
    paragraph = container.find('p')
    assert paragraph is not None
    assert paragraph.string.strip() == 'Thank you for completing this page.'

    # Check form
    form = container.find('form', action='/calculate_score', method='get')
    assert form is not None

    # Check button
    button = form.find('button', type='submit', id='finalSubmitButton')
    assert button is not None
    assert button.string.strip() == 'Finish'
