import functools

from flask import Blueprint
from flask_login import current_user
from flask_socketio import emit, send, disconnect

from server.socket import socketio


sockets = Blueprint('sockets', __name__)


def authenticated_socket(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped


NAMESPACE_TEST = '/socket/test'


@socketio.on('connect', namespace=NAMESPACE_TEST)
@authenticated_socket
def test_socket_connect():
    send('connected to /socket/test')


@socketio.on('disconnect', namespace=NAMESPACE_TEST)
@authenticated_socket
def test_socket_disconnect():
    print('client disconnected from test socket')


@socketio.on('message', namespace=NAMESPACE_TEST)
@authenticated_socket
def test_bounce_message(message):
    print('received message: ' + message)
    send(message)


@socketio.on('json', namespace=NAMESPACE_TEST)
@authenticated_socket
def test_bounce_json(json):
    print('received json: ' + str(json))
    send(json, json=True)
