def test_webapp_no_auth(client):
    response = client.get('/webapp')

    assert(response.status_code == 301)
