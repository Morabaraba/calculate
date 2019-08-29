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