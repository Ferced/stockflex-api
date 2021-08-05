import mongoengine as db
from flask import Flask
from flask.app import Flask
from flask_bcrypt import Bcrypt

from .config import config_by_name

flask_bcrypt = Bcrypt()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    # TODO: pasar la url de mongo a un config o algo ni idea.
    db.connect(host="mongodb://0.0.0.0:2717/reverse-proxy-test")
    flask_bcrypt.init_app(app)

    return app
