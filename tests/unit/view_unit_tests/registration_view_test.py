import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_registration_page_render(client):
    response = client.get('/registration')
    assert response.status_code == 200

    # Parse the HTML
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Check title
    assert soup.title.string == 'Registration Page'

    # Check form attributes
    form = soup.find('form')
    assert form['action'] == "/registration"
    assert form['method'] == 'post'

    # Check input fields
    username_input = soup.find('input', {'id': 'username'})
    assert username_input is not None
    assert username_input['name'] == 'username'
    assert username_input['type'] == 'text'
    assert 'required' in username_input.attrs
    
    fname_input = soup.find('input', {'id': 'fname'})
    assert fname_input is not None
    assert fname_input['name'] == 'fname'
    assert fname_input['type'] == 'text'
    assert 'required' in fname_input.attrs
    
    lname_input = soup.find('input', {'id': 'lname'})
    assert lname_input is not None
    assert lname_input['name'] == 'lname'
    assert lname_input['type'] == 'text'
    assert 'required' in lname_input.attrs
    
    email_input = soup.find('input', {'id': 'email'})
    assert email_input is not None
    assert email_input['name'] == 'email'
    assert email_input['type'] == 'email'
    assert 'required' in email_input.attrs

    pwd_input = soup.find('input', {'id': 'pwd'})
    assert pwd_input is not None
    assert pwd_input['name'] == 'pwd'
    assert pwd_input['type'] == 'password'
    assert 'required' in pwd_input.attrs

    cpwd_input = soup.find('input', {'id': 'cpwd'})
    assert cpwd_input is not None
    assert cpwd_input['name'] == 'cpwd'
    assert cpwd_input['type'] == 'password'
    assert 'required' in cpwd_input.attrs

    # Check buttons
    registration_button = soup.find('input', {'value': 'Submit'})
    assert registration_button['type'] == "submit"

    # BacK button
    back_button = soup.find('button', string='Back')
    assert back_button is not None
    assert back_button['onclick'] == "history.back();"

def test_registration_page_post_failure(client):
    response = client.post('/registration', data={
        'username': 'wronguser',
        'fname': 'wrongname',
        'lname': 'wronglastname',
        'email': 'wrongemail',
        'pwd': 'wrongpassword',
        'cpwd': 'wrongpassword'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == '/registration'