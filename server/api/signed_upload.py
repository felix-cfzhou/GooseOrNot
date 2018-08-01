import boto3
import uuid

from flask import Blueprint, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from server.views import jsonResponse
from server.database import db
from server.models.image import Image
from config import Config


def get_unique_secure_filename(filename):
    clean_name = secure_filename(filename)
    unique_name = str(uuid.uuid4()) + clean_name

    return unique_name


s3_bucket = Config.S3_BUCKET_NAME
access_key_id = Config.AWS_ACCESS_KEY_ID
access_key = Config.AWS_SECRET_ACCESS_KEY
bucket_location = 'http://{}.s3.amazonaws.com/'.format(s3_bucket)

s3 = boto3.client(
        "s3",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=access_key
        )


def upload_file_to_s3(file, acl="public-read"):
    unique_secure_filename = get_unique_secure_filename(file.filename)

    try:
        s3.upload_fileobj(
                file,
                s3_bucket,
                unique_secure_filename,
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                    }
                )
    except Exception as e:
        print("error: ", e)
        return e

    eventual_url = "{}{}".format(bucket_location, unique_secure_filename)
    return eventual_url, unique_secure_filename


signed_upload = Blueprint('signed_upload', __name__, url_prefix='/api')


@signed_upload.route('/signed_upload', methods=['POST'])
@login_required
def signed_s3():
    file = request.files["upload_file"]

    if file.filename == "":
        return jsonResponse(
                {"signed_upload": "not file uploaded"},
                400
                )

    s3_url, unique_secure_filename = upload_file_to_s3(file)

    with current_app.app_context():
        session = db.session
        image = Image(
                file_name=unique_secure_filename,
                user_id=current_user.id,
                url=s3_url
                )
        session.add(image)

    return jsonResponse(
            {
                "signed_upload": "success",
                "url": s3_url
                },
            200
            )
