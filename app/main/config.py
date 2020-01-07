import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret')
    DEBUG = False


class Development(Config):

    DEBUG = True


class Test(Config):

    DEBUG = True
    TESTING = True


class Production(Config):

    DEBUG = False


config_by_name = dict(
    dev=Development,
    test=Test,
    prod=Production
)

key = Config.SECRET_KEY
