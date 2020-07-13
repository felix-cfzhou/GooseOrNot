from server.database import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
            )
    file_name = db.Column(
            db.String(),
            nullable=False,
            unique=True
            )
    user_id = db.Column(
            db.Integer,
            db.ForeignKey('users.id', name='FK_users_images')
            )
    tasks = db.relationship(
            'Task',
            backref='image',
            lazy='dynamic'
            )
    is_goose = db.Column(
            db.Boolean,
            nullable=True,
            )
    url = db.Column(
            db.String(),
            nullable=False,
            unique=True
            )
    timestamp = db.Column(
            db.DateTime,
            index=True,
            default=db.func.now()
            )

    def __repr__(self):
        return '<id {}:{}>'.format(self.id, self.file_name)
