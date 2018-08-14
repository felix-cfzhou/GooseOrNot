from flask_script import Manager
from flask_migrate import MigrateCommand

from server.factory import create_app
from server.models.task import Task  # noqa: F401
from server.models.user import User  # noqa: F401

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
