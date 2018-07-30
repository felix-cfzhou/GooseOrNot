def login(client, username, password):
    return client.post(
            '/login',
            data=dict(
                username=username,
                password=password
                ),
            follow_redirects=True
            )


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_login_logout(client, user):
    response = login(client, 'username', 'password')

    assert(response.status_code == 200)

    response = logout(client)

    assert(response.status_code == 200)


def test_webapp_no_auth(client):
    response = client.get('/webapp')

    assert(response.status_code == 301)
