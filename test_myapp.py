# test_hello.py
from myapp import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hey, this is my test app!!'
