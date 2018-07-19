from os import path
import uuid
import json

from flask import Blueprint, Response, current_app, request
from werkzeug.utils import secure_filename
from server.models.image import Image
from server.database import db


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


NoFile = {"error": "no files uploaded"}


def jsonResponse(dictionary, status_code):
    return Response(json.dumps(dictionary), status_code)


@upload.route('/photos', methods=['POST'])
def receive():
    if 'photo' in request.files:
        responseDict = {}
        for file in request.files.getlist('photo'):
            filename = file.filename
            if filename == '':
                responseDict[filename] = "not a photo"
            elif not allowed_file(filename):
                responseDict[filename] = "file type not allowed"
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
                responseDict[filename] = "success"
        return jsonResponse(responseDict, 200)
    else:
        return jsonResponse(NoFile, 200)
