import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with client.session_transaction() as sess:
            # Simulate a logged-in user by adding 'username' to the session
            sess['username'] = 'testuser'
        yield client

def test_user_profile_page_render(client):
    """Test if User Profile page renders correctly"""
    response = client.get('/')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check title
    assert soup.title.string == 'Home Page'

    # Check main section
    main = soup.find('div', {'class': 'main'})
    assert main is not None
    start_button = main.find('button')
    assert start_button is not None
    assert 'onclick' in start_button.attrs
    assert start_button['onclick'] == "window.location.href='/PageOneDigitalStrategy';"