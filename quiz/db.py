from flask import current_app, g
from flask_mongoengine import MongoEngine


def get_db():
    """Get database from g object. If database does not exist in g object it will
    init database.
    """

    if "db" not in g:
        g.db = MongoEngine()
        g.db.init_app(current_app)

    return g.db


def close_db():
    """Close current database."""

    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Init Db."""

    db = get_db()

    # call close_db when cleanup is up after returning response
    current_app.teardown_appcontext(close_db)
