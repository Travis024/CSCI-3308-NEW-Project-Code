import os
basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES = {
    'user': 'matt',
    'pw': 'matt',
    'db': 'livboulder',
    'host': 'localhost',
    'port': '5432',
}

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SecretKey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
