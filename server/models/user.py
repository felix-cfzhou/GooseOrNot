from server.database import db
from server.login import login_manager
from server.models.task import Task
from server.models.image import Image

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
            )
    username = db.Column(
            db.String(),
            index=True,
            unique=True,
            nullable=False
            )
    email = db.Column(
            db.String(),
            index=True,
            unique=True,
            nullable=False
            )
    password_hash = db.Column(
            db.String(),
            nullable=False,
            )
    tasks = db.relationship(
            'Task',
            backref='user',
            lazy='dynamic'
            )
    images = db.relationship(
            'Image',
            backref='user',
            lazy='dynamic'
            )

    def __repr__(self):
        return '<User {}:{}>'.format(
                self.id,
                self.username
                )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add_image(self, file_name):
        im = Image(file_name=file_name, user_id=self.id)
        db.session.add(im)
        return im

    def get_images(self):
        return Image.query.filter_by(user_id=self.id)

    def launch_task(self, task, params, name, description, priority, *args, **kwargs):
        rq_job = current_app.task_queues[priority].enqueue_call(func=task, args=params, *args, **kwargs)
        task = Task(id=rq_job.get_id(), name=name, description=description, user_id=self.id)
        db.session.add(task)
        return task

    def get_tasks_in_progress(self, name):
        return Task.query.filter_by(name=name, user_id=self.id, complete=False).all()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
