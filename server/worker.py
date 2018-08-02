from rq import Worker, Queue, Connection

from server.factory import create_app
from server.redis import conn


app = create_app()
app.app_context().push()

listen = ['high', 'default', 'low']


if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
