import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
basedir = os.path.abspath(os.path.dirname(__file__))
os.environ["REVERSEPROXY_ENV"] = "dev"


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "DFJ8F2382RJSDFJ238922TJWE3FWEFWJE2")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = os.environ["MONGO_HOST"]
    MONGODB_PORT = int(os.environ["MONGO_PORT"])
    MONGODB_NAME = os.environ["MONGO_DB"]
    MONGODB_USERNAME = os.environ["MONGO_USERNAME"]
    MONGODB_PASSWORD = os.environ["MONGO_PASSWORD"]
    MONGODB_AUTH_SOURCE = os.environ["MONGO_AUTH_SOURCE"]
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGODB_HOST = os.environ["MONGO_HOST"]
    MONGODB_PORT = int(os.environ["MONGO_PORT"])
    MONGODB_NAME = os.environ["MONGO_DB"]
    MONGODB_USERNAME = os.environ["MONGO_USERNAME"]
    MONGODB_PASSWORD = os.environ["MONGO_PASSWORD"]
    MONGODB_AUTH_SOURCE = os.environ["MONGO_AUTH_SOURCE"]
    REDIS_HOST = "localhost"
    REDIS_PORT = "6379"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    MONGODB_HOST = os.environ["MONGO_HOST"]
    MONGODB_PORT = int(os.environ["MONGO_PORT"])
    MONGODB_NAME = os.environ["MONGO_DB"]
    MONGODB_USERNAME = os.environ["MONGO_USERNAME"]
    MONGODB_PASSWORD = os.environ["MONGO_PASSWORD"]
    MONGODB_AUTH_SOURCE = os.environ["MONGO_AUTH_SOURCE"]
    REDIS_HOST = "redis"
    REDIS_PORT = "6379"
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
