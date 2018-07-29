from server.factory import create_app
from server.socket import socketio


if __name__ == "__main__":
    app = create_app()
    socketio.run(app, debug=True)
