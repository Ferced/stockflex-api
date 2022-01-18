import os
import unittest
from flask_cors import CORS
from flask_script import Manager
from app import blueprint
from app.main import create_app

env_name = "test"

app = create_app()

CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(host="0.0.0.0", port="3031")


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
