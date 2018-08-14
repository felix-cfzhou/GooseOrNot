import io

import boto3
from moto import mock_s3
from werkzeug import FileStorage

from server.api.image.upload import s3_bucket, upload_file_to_s3


def test_unauth_signed_upload(client):
    response = client.post(
            '/api/image',
            data=dict(
                upload_file=(
                    io.BytesIO(b'test'),
                    'test.csv'
                    )
                )
            )

    assert(response.status_code == 403)


@mock_s3
def test_boto3_upload_file_func():
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket=s3_bucket)

    file = FileStorage(
            filename='test.txt',
            stream=io.BytesIO(b'test'),
            content_type='text'
            )

    s3_url, unique_secure_filename = upload_file_to_s3(file)

    body = conn.Object(s3_bucket, unique_secure_filename).get()['Body'].read().decode("utf-8")

    assert(body == 'test')
