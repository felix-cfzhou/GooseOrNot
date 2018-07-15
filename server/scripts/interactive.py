from server.factory import create_app
from server.database import db


create_app().app_context().push()
session = db.session
