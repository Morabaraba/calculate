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


def test_ajax_subtraction(client):
    """Test our ajax subtraction call"""

    rv = client.get('/ajax/subtraction?number1=1&number2=2')
    result = rv.get_json()
    
    assert result['answer'] == '-1'


def test_ajax_multiplication(client):
    """Test our ajax multiplication call"""

    rv = client.get('/ajax/multiplication?number1=1&number2=2')
    result = rv.get_json()
    
    assert result['answer'] == '2'


def test_ajax_division(client):
    """Test our ajax division call"""

    rv = client.get('/ajax/division?number1=1&number2=2')
    result = rv.get_json()
    
    assert result['answer'] == '0.5'
    

def test_ajax_division(client):
    """Test our ajax division call"""

    rv = client.get('/ajax/division?number1=1&number2=2')
    result = rv.get_json()
    
    assert result['answer'] == '0.5'



def test_ajax_division(client):
    """Test our ajax division call"""

    rv = client.get('/ajax/modulo?number1=4&number2=3')
    result = rv.get_json()
    
    assert result['answer'] == '1'
    



def test_ajax_sqrt(client):
    """Test our ajax sqrt call"""

    rv = client.get('/ajax/sqrt?number1=4')
    result = rv.get_json()
    
    assert result['answer'] == 2 # TODO fix other test to return JSON datatype Number instead of string