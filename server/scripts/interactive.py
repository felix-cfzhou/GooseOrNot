from server.factory import create_app
from server.database import db

from server.models.user import User


app = create_app()
app.app_context().push()

connection = db.engine.connect()
transaction = connection.begin()

options = dict(bind=connection, binds={})
session = db.create_scoped_session(options=options)

db.session = session
