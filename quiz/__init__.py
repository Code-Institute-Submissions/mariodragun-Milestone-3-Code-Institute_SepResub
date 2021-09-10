import os
from flask import Flask
from .db import get_db


# Application Factory
def create_app(test_config=None):

    # init flask app
    app = Flask(__name__, instance_relative_config=True)

    # add basic configurations from env variables
    app.config.from_mapping(SECRET_KEY=os.getenv("SECRET_KEY"), MONGODB_HOST=os.getenv("MONGODB_HOST"))

    # ensure that instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # get database and init it within app context
    with app.app_context():
        db = get_db()
        db.init_app(app)

    return app
