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
            sess['password'] = 'password'
        yield client

def test_login_page_render(client):
    """Test if the login page renders correctly."""
    response = client.get('/login')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check title
    assert soup.title.string == "Login Page"

    # Check form attributes
    form = soup.find('form')
    assert form['action'] == "/login"
    assert form['method'] == "post"

    # Check input fields
    username_input = soup.find('input', {'name': 'username'})
    assert username_input['type'] == "text"
    assert username_input['id'] == "username"
    assert 'required' in username_input.attrs

    password_input = soup.find('input', {'name': 'password'})
    assert password_input['type'] == "password"
    assert password_input['id'] == "password"
    assert 'required' in password_input.attrs

    # Check stylesheets
    stylesheets = soup.find_all('link', rel='stylesheet')
    expected_stylesheets = [
        '/static/content/login-page.css'
    ]
    hrefs = [link['href'] for link in stylesheets]
    for stylesheet in expected_stylesheets:
        assert stylesheet in hrefs

    # Check meta tags
    meta_charset = soup.find('meta', attrs={'charset': 'UTF-8'})
    meta_viewport = soup.find('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'})
    meta_compat = soup.find('meta', attrs={'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'})
    assert meta_charset is not None
    assert meta_viewport is not None
    assert meta_compat is not None

    # Check buttons
    login_button = soup.find('input', {'value': 'Login'})
    assert login_button['type'] == "submit"

    register_button = soup.find('input', {'value': 'Register'})
    assert register_button['type'] == "button"
    assert register_button['onclick'] == "window.location='/registration';"

def test_login_page_post_failure(client):
    """Test posting to the login endpoint with invalid credentials."""
    response = client.post('/login', data={
        'username': 'invaliduser',
        'password': 'invalidpassword'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == '/login'
