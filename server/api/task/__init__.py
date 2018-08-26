from flask import Blueprint
from flask_login import current_user
from flask_restful import Api, Resource, reqparse

from server.database import db
from server.models.image import Image
from server.models.task import Task
from server.api import authenticated_endpoint
from server.tasks.predict import async_is_goose


task_endpoint = Blueprint('task_endpoint', __name__)
task_api = Api(task_endpoint, prefix='/api')


class TaskEndpoint(Resource):

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('image_id', required=True, type=int, location='form')

    @authenticated_endpoint
    def post(self):
        args = self.post_parser.parse_args()
        image_id = args['image_id']

        image = Image.query.filter_by(id=image_id).first()
        task = async_is_goose(image)
        json = dict(id=task.id, image_id=task.image_id)

        return json, 200

    @authenticated_endpoint
    def get(self):
        images = current_user.images

        def get_image_tasks(image):
            return image.tasks.order_by(db.desc(Task.id))[-5:]

        def parse_task(task):
            return dict(id=task.id, complete=task.complete)

        json = [parse_task(t) for t in [get_image_tasks(im) for im in images]]

        return json, 200


task_api.add_resource(TaskEndpoint, '/task')
