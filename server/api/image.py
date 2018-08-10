from flask import Blueprint
from flask_login import current_user, login_required
from flask_restful import Api, Resource, reqparse


image_query = Blueprint('image_query', __name__)
image_query_api = Api(image_query, prefix='/api')


class ImageQuery(Resource):

    post_parser = reqparse.RequestParser()

    @login_required
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


image_query_api.add_resource(ImageQuery, '/image/query')
