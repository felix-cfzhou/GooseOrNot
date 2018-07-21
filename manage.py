from flask_script import Manager
from flask_migrate import MigrateCommand

from server.factory import create_app
from server.models.task import Task
from server.models.user import User

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
