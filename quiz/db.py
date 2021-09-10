from flask import g
from flask_mongoengine import MongoEngine


def get_db():
    """Get database from g object. If database does not exist in g object it will initialize MonogEngine() instance."""

    if "db" not in g:
        g.db = MongoEngine()

    return g.db
