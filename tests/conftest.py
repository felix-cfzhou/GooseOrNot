import pytest

from flask_migrate import upgrade, downgrade
from fakeredis import FakeStrictRedis
from rq import Queue

from server.factory import create_app
from server.database import db as _db
from server.models.user import User
from server.models.image import Image
from server.models.task import Task
from config import TestingConfig


@pytest.fixture(scope='session')
def queue():
    return Queue(is_async=False, connection=FakeStrictRedis())


@pytest.fixture(scope='session')
def app(request):
    '''Session-wide test application'''
    app = create_app(TestingConfig)

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def client(app):
    client = app.test_client()

    return client


@pytest.fixture(scope='session')
def db(app, request):
    '''Session-wide test database'''

    def teardown():
        downgrade(directory='migrations', revision='base')

    _db.app = app
    upgrade(directory='migrations', revision='head')

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='session')
def session(db, request):
    '''New database session for a test.'''
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def user(session, request):
    user = User(username='username', email='example@example.com')
    user.set_password('password')
    session.add(user)
    session.commit()

    def teardown():
        session.delete(user)
        session.commit()

    request.addfinalizer(teardown)
    return user
