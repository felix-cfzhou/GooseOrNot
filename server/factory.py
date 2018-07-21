import os
from rq import Queue

from flask import Flask
from flask_migrate import Migrate

from server.database import db
from server.views import home
from server.views.upload import upload
from server.worker import conn


migrate = Migrate()

def create_dir_if_none(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    create_dir_if_none(app.config['PHOTO_UPLOAD_FOLDER'])
    db.init_app(app)
    migrate.init_app(app, db)
    app.task_queues = {
            'high': Queue('high', connection=conn),
            'default': Queue('default', connection=conn),
            'low': Queue('low', connection=conn)
            }
    app.register_blueprint(home)
    app.register_blueprint(upload)
    return app
