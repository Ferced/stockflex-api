import mongoengine as db
from flask.app import Flask

# from redis import Redis
import os
from .config import config_by_name
from flask_bcrypt import Bcrypt

config_env = os.getenv("REVERSEPROXY_ENV", default="dev")
config = config_by_name[config_env]
# redis_client = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)

db.connect(
    config.MONGODB_NAME,
    port=config.MONGODB_PORT,
    username=config.MONGODB_USERNAME,
    password=config.MONGODB_PASSWORD,
    authentication_source=config.MONGODB_AUTH_SOURCE,
)
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_env])
    flask_bcrypt.init_app(app)
    return app
