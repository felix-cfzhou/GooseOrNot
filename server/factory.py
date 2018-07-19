import os

from flask import Flask
from flask_migrate import Migrate

from server.database import db
from server.views import home
from server.views.upload import upload


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(home)
    app.register_blueprint(upload)
    return app
