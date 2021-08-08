import mongoengine as db
from flask.app import Flask
from redis import Redis
import os
from .config import config_by_name


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    return app

class Connections():
    config_name = os.getenv("REVERSEPROXY_ENV") or "dev"
    config = config_by_name[config_name]

    redis_client = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

    db.connect(config.MONGODB_NAME,host=config.MONGODB_HOST,port=config.MONGODB_PORT)