from flask import Flask
import os


from flask_mongoengine import MongoEngine

# init flask app
app = Flask(__name__)

# adding configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# add configuration for MongoDB Cluster
app.config["MONGODB_HOST"] = os.getenv("MONGODB_HOST")

# init mongo database and attach it to the app
db = MongoEngine()
db.init_app(app)
