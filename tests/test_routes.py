from flask import url_for
from web_dev import app

def test_views_endpoint():
    # init flask
    client = app.test_client()
    
    # get response from views
    response = client.get('/')

    # check status code
    assert response.status_code == 200, 'FAILED'
    
    # check in html code
    assert b'<h1>Home</h1>' in response.data, 'N/A in HTML'

def test_views_url_for():
    with app.test_request_context():
        assert url_for('index') == '/', 'Route Error'