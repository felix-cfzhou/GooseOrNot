import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    BASE_DIR = basedir
    #  TODO: reconfigure upload come time to like /var or smt
    PHOTO_UPLOAD_FOLDER = os.path.join(basedir, 'server/.photos')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'f581bc8d046733c56164ec6187ab14469d0dc77e9092ed23'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    REDIS_URL = os.environ.get('REDISTOGO_URL', 'redis://localhost:6379')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'gooseornot'
    MAIL_PASSWORD = 'waterlooCS'
    MAIL_DEFAULT_SENDER = 'gooseornot@gmail.com'
    SERVER_NAME = os.environ['SERVER_NAME']
    S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

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
