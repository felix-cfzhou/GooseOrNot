import os

from flask import Flask
from flask_migrate import Migrate

from database import db
from views import home


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(home)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
