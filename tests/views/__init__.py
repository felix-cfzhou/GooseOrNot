import json


def post_json(client, path, dictionary):
    response = client.post(
            path,
            content_type='application/json',
            data=json.dumps(dictionary)
            )

    return response


def test_home_page(client):
    response = client.get('/')

    assert(response.status_code == 200)


def test_login_nonexisiting_user(client):
    response = post_json(
            client,
            '/login',
            {
                'username': 'non_existant_user',
                'password': 'password'
                }
            )

    assert(response.status_code == 400)


def test_login_wrong_password(client, user):
    response = post_json(
            client,
            '/login',
            {
                'username': 'username',
                'password': 'wrong_password',
                }
            )

    assert(response.status_code == 400)


def test_login_correct(client, user):
    response = post_json(
            client,
            '/login',
            {
                'username': 'username',
                'password': 'password',
                }
            )

    assert(response.status_code == 200)
