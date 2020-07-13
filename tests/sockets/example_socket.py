import pytest
from flask_socketio import SocketIOTestClient

from server.socket import socketio
from server.sockets import NAMESPACE_TEST


@pytest.mark.xfail
def test_socket_test(app, logged_in_user):
    client = SocketIOTestClient(app, socketio, namespace=NAMESPACE_TEST)
    client.send('message')
    print(client.get_received())

    assert(False)
