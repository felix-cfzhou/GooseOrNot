from server.factory import create_app
from server.database import db

from server.models.user import User  # noqa: F401


app = create_app()
app.app_context().push()

session = db.session
