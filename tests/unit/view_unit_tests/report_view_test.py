import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['username'] = 'testuser'
        yield client

def test_report_page_render(client):
    """Test if Report page renders correctly"""
    response = client.get('/ReportPage')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Submit Page'

    # Check header
    header = soup.find('div', {'id': 'header-placeholder'})
    assert header is not None
    
    # Check for presence of h1 tag directly in the main content
    main_content = soup.find('div', {'class': 'main'})
    assert main_content is not None
    h1_tag = main_content.find('h1')
    assert h1_tag is not None
    assert h1_tag.string == 'Assessment Overview'
    
    # Check footer
    footer = soup.find('div', {'id': 'footer-placeholder'})
    assert footer is not None