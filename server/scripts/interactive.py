from server.factory import create_app
from server.database import db

from server.models.user import User


app = create_app()
app.app_context().push()

session = db.session
