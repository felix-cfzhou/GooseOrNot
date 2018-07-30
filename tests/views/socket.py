def test_socket(client):
    response = client.get('/webapp/socket')

    assert(response.status_code == 302)
