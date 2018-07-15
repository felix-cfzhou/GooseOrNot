from app import create_app
from database import db


create_app().app_context().push()
session = db.session
