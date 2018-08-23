import requests as req


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000/')
    assert response.status_code == 200


def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000/')
    assert 'Try something like this: http http://127.0.0.1:5000/cow?msg="hello world"' in str(response.text)


def test_server_get_with_querystring_test_route_status_400():
    response = req.get('http://127.0.0.1:5000/test?category=correct')
    assert response.status_code == 400


def test_server_get_with_bad_querystring_test_route_status_400():
    response = req.get('http://127.0.0.1:5000/test?incorrect=querystring')
    assert response.status_code == 400


def test_server_get_no_querystring_test_route_status_400():
    response = req.get('http://127.0.0.1:5000/test')
    assert response.status_code == 400


def test_server_get_home_route_status_404():
    response = req.get('http://127.0.0.1:5000/failure')
    assert response.status_code == 404


def test_server_post_home_route_status_201():
    response = req.post('http://127.0.0.1:5000/')
    assert response.status_code == 404


def test_server_put_not_implemented_status_501():
    response = req.put('http://127.0.0.1:5000/')
    assert response.status_code == 501


def test_server_delete_not_implemented_status_501():
    response = req.delete('http://127.0.0.1:5000/')
    assert response.status_code == 501
