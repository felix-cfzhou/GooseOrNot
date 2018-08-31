from flask import Blueprint
from flask_login import current_user
from flask_socketio import send, join_room

from server.socket import socketio
from server.sockets import authenticated_socket


socket_general = Blueprint('socket_general', __name__)


NAMESPACE_TEST = '/socket/general'


@socketio.on('connect', namespace=NAMESPACE_TEST)
@authenticated_socket
def general_socket_connect():
    join_room(str(current_user.id))
    send('connected to /socket/general')


@socketio.on('disconnect', namespace=NAMESPACE_TEST)
@authenticated_socket
def general_socket_disconnect():
    print('client disconnected from test socket')
