from flask import Flask
import os

from flask_mongoengine import MongoEngine
import mongoengine as me
import datetime

# init flask app
app = Flask(__name__)

# adding configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# add configuration for MongoDB Cluster
app.config["MONGODB_HOST"] = os.getenv("MONGODB_HOST")

# init mongo database and attach it to the app
db = MongoEngine()
db.init_app(app)


#### DB Models
# define db models to create collections in MongoDB
# define basic User Model - to register/login or use User information
# use me as mongoengine alias. And for each field define what type it is.
class User(me.Document):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    #  username is set to be unique to prevent multiple users to have same username
    username = me.StringField(required=True, unique=True)
    # email is set to be unique to prevent multiple users to have same email
    email = me.EmailField(required=True, unique=True)
    # password is set to be a plain text field - because we will use generate_password_hash so
    #  there is no need to hash it again
    password = me.StringField(max_length=256)


# Question - list of answers (one or many can be true)
class Answer(me.EmbeddedDocument):
    # answer basic text
    answer = me.StringField(required=True)
    # is correct boolean, will signify if the answer is correct or not
    is_correct = me.BooleanField(default=False)

    # standard datetime field which will be updated every time Question is modified
    # and that is why the default value datetime.datetime.now which is the now date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)


class Question(me.Document):
    # stanard question text title
    title = me.StringField(required=True, unique=True)
    # help text for the question - additional explanation of the question, not required
    description = me.StringField(default="")
    # url field for the images, also additional explanations of the questions
    image = me.URLField(required=False)
    # embeded document, one question can have many answers (List of answers)
    answers = me.ListField(me.EmbeddedDocumentField(Answer))

    # standard datetime field which will be updated every time Question is modified
    # and that is why the default value datetime.datetime.now which is the now date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)
