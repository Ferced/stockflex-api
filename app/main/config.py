import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "SDFJ8F2382RJSDFJ238922TJWE3FWEFWJE2")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGOENGINE_DATABASE_URI = "mongodb://0.0.0.0:2717/reverse-proxy-test"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGOENGINE_DATABASE_URI = "mongodb://0.0.0.0:2717/reverse-proxy-test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
