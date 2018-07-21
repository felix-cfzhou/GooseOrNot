from server.database import db
from server.models.task import Task
from server.models.image import Image


class User(db.Model):
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
