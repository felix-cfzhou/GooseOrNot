from flask import Blueprint


home = Blueprint('home', __name__, url_prefix='')


@home.route('/')
def hello():
    return "Hello!"
