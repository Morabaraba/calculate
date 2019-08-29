import pytest

from calculate import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_index(client):
    """Test our hello."""

    rv = client.get('/')
    #import pdb; pdb.set_trace()
    assert rv.status == '200 OK'
    
def test_ajax_addition(client):
    """Test our ajax addition call"""

    rv = client.get('/ajax/addition?number1=1&number2=2')
    result = rv.get_json()
    
    assert result['answer'] == '3'