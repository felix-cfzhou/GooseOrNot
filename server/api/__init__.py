import functools

from flask import Blueprint, abort
from flask_restful import Api, Resource, reqparse
from flask_login import current_user, login_user, logout_user

from server.models.user import User


def authenticated_endpoint(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(403)
        else:
            return f(*args, **kwargs)
    return wrapped


restful_home = Blueprint('api_home', __name__)
restful_home_api = Api(restful_home, prefix='/api')


class Login(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            json = dict(
                    username="invalid username or password",
                    password="invalid username or password"
                    )
            return json, 400

        login_user(user)
        return {}, 200


class Logout(Resource):

    @authenticated_endpoint
    def post(self):
        logout_user()

        return {}, 200


restful_home_api.add_resource(Login, '/login')
restful_home_api.add_resource(Logout, '/logout')
