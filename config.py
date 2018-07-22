import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BASE_DIR = basedir
    #  TODO: reconfigure upload come time to like /var or smt
    PHOTO_UPLOAD_FOLDER = os.path.join(basedir, 'server/.photos')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-will-be-changed'  # TODO: changed secret key
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    REDIS_URL = os.environ.get('REDISTOGO_URL', 'redis://localhost:6379')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gooseornot'
    MAIL_PASSWORD = 'waterlooCS'
    MAIL_DEFAULT_SENDER = 'gooseornot@gmail.com'
    SERVER_NAME = os.environ['SERVER_NAME']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['TESTING_DATABASE_URL']
    TESTING = True
