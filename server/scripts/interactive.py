from server.factory import create_app
from server.database import db


app = create_app()
app.app_context().push()
session = db.session
