import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_footer_template_render(client):
    """Test if footer template renders correctly"""
    response = client.get('/AssessmentFooterTemplate')
    assert response.status_code == 200

        # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')

    # Check title
    assert soup.title.string == 'Digitial Assessment Footer'