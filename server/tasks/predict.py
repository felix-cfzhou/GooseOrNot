from os import path
from uuid import uuid4

import requests
from rq import get_current_job
from flask import current_app
from flask_login import current_user

from server.ml.boost import is_goose
from server.socket import socketio
from server.models.task import Task
from server.database import db


def task_is_goose(image):
    home_path = path.expanduser('~')
    im_path = path.join(home_path, '.tmp/GooseOrNot/pic', image.file_name)

    req = requests.get(image.url)
    open(im_path, 'wb').write(req.content)

    pred = is_goose(im_path)
    response = dict(id=image.id, isGoose=pred)

    socketio.emit('task is goose', response, room=current_user.id)

    image.is_goose = pred
    job = get_current_job()
    task = Task.query.filter_by(id=job.get_id()).first()
    task.complete = True

    db.session.commit()


def async_is_goose(image):
    job_id = str(uuid4())

    task = Task(
            id=job_id,
            name='task_is_goose',
            description='predict if image is of a goose or not',
            user_id=current_user.id,
            image_id=image.id,
            )

    db.session.add(task)
    db.session.commit()

    current_app.task_queues['high'].enqueue_call(
            func=task_is_goose,
            args=(image,),
            job_id=job_id
            )

    return task
