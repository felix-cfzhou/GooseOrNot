from server.database import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    file_name = db.Column(db.String(), nullable=False)

    def __init__(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return '<id {}>'.format(self.id)
