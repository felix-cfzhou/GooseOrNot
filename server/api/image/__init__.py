from flask import Blueprint, current_app, abort
from flask_login import current_user
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage

from server.database import db
from server.models.image import Image
from server.api import authenticated_endpoint
from server.api.image.upload import upload_file_to_s3


image_endpoint = Blueprint('image_endpoint', __name__)
image_api = Api(image_endpoint, prefix='/api')


IMAGES = set([
        'jpg',
        'jpeg',
        'jpe',
        'png',
        'tif',
        'tiff',
        'fpx'
        ])


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in IMAGES


class FileStorageArgument(reqparse.Argument):
    """argument class for flask-restful used
    in all cases where file uploads need to be handled"""

    def convert(self, value, op):
        if self.type is FileStorage:
            return value
        else:
            # TODO: Not sure what this does, will investigate
            super(FileStorageArgument, self).convert(*args, **kwargs)  # noqa: F821


class ImageEndpoint(Resource):

    post_parser = reqparse.RequestParser(argument_class=FileStorageArgument)
    post_parser.add_argument('upload_file', required=True, type=FileStorage, location='files')

    @authenticated_endpoint
    def post(self):
        args = self.post_parser.parse_args()
        file = args['upload_file']

        if not allowed_file(file.filename):
            abort(400)

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

    @authenticated_endpoint
    def get(self):
        images = current_user.images

        json = []
        for im in images:
            json.append({
                "id": im.id,
                "file_name": im.file_name,
                "url": im.url
                })

        return json, 200


image_api.add_resource(ImageEndpoint, '/image')
