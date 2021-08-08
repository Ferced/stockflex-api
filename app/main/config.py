import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "SDFJ8F2382RJSDFJ238922TJWE3FWEFWJE2")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = "0.0.0.0"
    MONGODB_PORT = 2718
    MONGODB_NAME = "reverse-proxy"
    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = "7001"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_HOST = "0.0.0.0"
    MONGODB_PORT = 2718
    MONGODB_NAME = "reverse-proxy"
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    MONGODB_HOST = "mongodb"
    MONGODB_PORT = 27017
    MONGODB_NAME = "reverse-proxy"
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
