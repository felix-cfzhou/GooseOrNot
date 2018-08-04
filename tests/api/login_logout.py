def test_api_login_error(client, user):
    response = client.post(
            '/api/login',
            data=dict(
                username='fake',
                password='fake'
                )
            )

    assert(response.status_code == 400)


def test_api_login_success(client, user):
    response = client.post(
            '/api/login',
            data=dict(
                username='username',
                password='password'
                )
            )

    assert(response.status_code == 204)
