import io

def test_unauth_signed_upload(client):
    response = client.post(
            '/api/signed_upload',
            data=dict(
                upload_file=(
                    io.BytesIO(b'test'),
                    'test.csv'
                    )
                )
            )

    assert(response.status_code == 403)
