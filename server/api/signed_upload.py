import boto3
import uuid

from flask import Blueprint, current_app
from flask_login import current_user, login_required
from flask_restful import Api, Resource, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

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
bucket_location = 'https://{}.s3.amazonaws.com/'.format(s3_bucket)

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


signed_upload = Blueprint('signed_upload', __name__)
signed_upload_api = Api(signed_upload, prefix='/api')


class FileStorageArgument(reqparse.Argument):
    """argument class for flask-restful used
    in all cases where file uploads need to be handled"""

    def convert(self, value, op):
        if self.type is FileStorage:
            return value
        else:
            # TODO: Not sure what this does, will investigate
            super(FileStorageArgument, self).convert(*args, **kwargs)  # noqa: F821


class SignedUpload(Resource):

    post_parser = reqparse.RequestParser(argument_class=FileStorageArgument)
    post_parser.add_argument('upload_file', required=True, type=FileStorage, location='files')

    @login_required
    def post(self):
        args = self.post_parser.parse_args()
        file = args['upload_file']

        s3_url, unique_secure_filename = upload_file_to_s3(file)

        # TODO: configure authentification
        with current_app.app_context():
            session = db.session
            image = Image(
                    file_name=unique_secure_filename,
                    user_id=current_user.id,
                    url=s3_url
                    )
            session.add(image)
            session.commit()

            json = dict(id=image.id, file_name=image.file_name, url=s3_url)

        return json, 200


signed_upload_api.add_resource(SignedUpload, '/signed_upload')
