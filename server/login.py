from flask_login import LoginManager
from flask import redirect, abort, request, url_for


login_manager = LoginManager()


@login_manager.unauthorized_handler
def authorization_bouncer():
    if request.method == 'GET':
        return redirect(url_for('home.login', next=request.endpoint))
    else:
        abort(403)
