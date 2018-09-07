import json


def test_registration(testapp):
    """
    """
    account = {
        'email': 'test@example.com',
        'password': 'hello',
    }

    response = testapp.post('/api/v1/auth/register', json.dumps(account))
    assert response.status_code == 201
    assert response.json['token']


def test_invalid_registration(testapp):
    """
    """
    account = {
        'email': 'test_two@example.com',
    }

    response = testapp.post('/api/v1/auth/register', json.dumps(account), status='4**')
    assert response.status_code == 400
    # import pdb; pdb.set_trace()


def test_login(testapp):
    """
    """
    account = {
        'email': 'test@example.com',
        'password': 'hello',
    }

    response = testapp.post('/api/v1/auth/login', json.dumps(account))
    assert response.status_code == 201
    assert response.json['token']


def test_location_lookup(testapp):
    """
    """
    response = testapp.get('/api/v1/lookup/98109')
    assert response.status_code == 200
    assert response.json['name'] == 'Seattle'


def test_invalid_lookup_methods(testapp):
    """
    """
    response = testapp.put('/api/v1/lookup/98109', status='4**')
    assert response.status_code == 405
    response = testapp.delete('/api/v1/lookup/98109', status='4**')
    assert response.status_code == 405
    response = testapp.post('/api/v1/lookup/98109', status='4**')
    assert response.status_code == 405


def test_create_location(testapp):
    """
    """
    account = {
        'email': 'test@example.com',
        'password': 'hello',
    }

    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']

    location = {
        'name': 'Seattle',
        'zip_code': 98109
    }
    testapp.authorization = ('Bearer', token)
    response = testapp.post('/api/v1/location', json.dumps(location))
    assert response.status_code == 201