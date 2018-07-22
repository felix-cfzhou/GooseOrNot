from os import path
import uuid

from flask import Blueprint, current_app, request
from werkzeug.utils import secure_filename
from server.models.image import Image
from server.database import db
from server.views import jsonResponse


upload = Blueprint('upload', __name__, url_prefix='/upload')

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


NoFile = {"upload": "no files uploaded"}


@upload.route('/photos', methods=['POST'])
def receive():
    if 'photo' in request.files:
        for file in request.files.getlist('photo'):
            filename = file.filename
            if filename == '':
                return jsonResponse(
                        {'upload': 'not a photo'},
                        400
                        )
            elif not allowed_file(filename):
                return jsonResponse(
                        {'upload': 'file type not allowed'},
                        400
                        )
            else:
                clean_name = secure_filename(file.filename)
                unique_name = str(uuid.uuid4()) + clean_name
                file.save(path.join(
                    current_app.config['PHOTO_UPLOAD_FOLDER'],
                    unique_name
                    ))
                with current_app.app_context():
                    session = db.session
                    image = Image(unique_name)
                    session.add(image)
                    # TODO: investigate whether this is actually ideal
                    session.commit()
                return jsonResponse(
                        {'upload': 'success'},
                        200
                        )
    else:
        return jsonResponse(NoFile, 400)
