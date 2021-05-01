from flask import Flask
import os
from flask_admin.base import Admin
from flask_admin.contrib.mongoengine.view import ModelView
from wtforms import Form, StringField, PasswordField, validators
from flask import request, redirect, render_template, flash, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash


from flask.json import jsonify


from flask_mongoengine import MongoEngine
import mongoengine as me
import datetime

# init flask app
app = Flask(__name__, static_folder="static", static_url_path="/assets")


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
    #  username is set to be unique to prevent multiple users to have same 
    # username
    username = me.StringField(required=True, unique=True)
    # email is set to be unique to prevent multiple users to have same email
    email = me.EmailField(required=True, unique=True)
    # password is set to be a plain text field - because we will use 
    # generate_password_hash so
    #  there is no need to hash it again
    password = me.StringField(max_length=256)


# Question - list of answers (one or many can be true)
class Answer(me.EmbeddedDocument):
    # answer basic text
    answer = me.StringField(required=True)
    # is correct boolean, will signify if the answer is correct or not
    is_correct = me.BooleanField(default=False)

    # standard datetime field which will be updated every time Question is 
    # modified
    # and that is why the default value datetime.datetime.now which is the now 
    # date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)



class Question(me.Document):
    # stanard question text title
    title = me.StringField(required=True, unique=True)
    # help text for the question - additional explanation of the question, not 
    # required
    description = me.StringField(default="")
    # url field for the images, also additional explanations of the questions
    image = me.URLField(required=False)
    # embeded document, one question can have many answers (List of answers)
    answers = me.ListField(me.EmbeddedDocumentField(Answer))

    # standard datetime field which will be updated every time Question is 
    # modified
    # and that is why the default value datetime.datetime.now which is the now 
    # date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)

# Embeded model for QuizTaken - holds questions and chosen answers
class QuestionsAnswered(me.EmbeddedDocument):
    question = me.ReferenceField(Question)
    chosen_answer = me.StringField()
    is_correct = me.BooleanField(default=False)

   

class QuizTaken(me.Document):
    user = me.ReferenceField(User)
    list_of_questions = me.ListField(
        me.EmbeddedDocumentField(QuestionsAnswered))
    number_of_questions = me.IntField()
    correct_answers = me.IntField(default=0)

    is_done = me.BooleanField(default=False)

    date_started = me.DateTimeField()
    date_modified = me.DateTimeField(default=datetime.datetime.now)

    @property
    def overall_score(self):
        return f"{self.correct_answers}/{self.number_of_questions}"





# init admin class
admin = Admin(app, name="Quiz", template_mode="bootstrap3")

# defining User Admin View which we will use on the Admin site of the Flask app
class UserAdminView(ModelView):
    column_filters = ["username", "email"]

# defining QuestionAdminView which we will use
class QuestionsAdminView(ModelView):
    column_filters = ["title"]

class QuizTakenAdminView(ModelView):
    column_filter = ["user"]


# connecting User and Question models with Admin
admin.add_view(UserAdminView(User))
admin.add_view(QuestionsAdminView(Question))
admin.add_view(QuizTakenAdminView(QuizTaken))
# helepr functions
# create/set user questions
def create_user_quiz():
    # get all questions
    all_questions = Question.objects()

    # get only id's from the Questions and set them in the list
    all_questions_id_list = [str(x.id) for x in all_questions]
    # randomize list of id's from this
    all_questions_id_list_random = random.sample(
        all_questions_id_list, k=all_questions.count())

    list_of_questions_generated_list = list()
    quiz_taken_number_of_questions_dict = {}
    # for all randomized id's get Question object and 
    # store it in a list_of_questions_generated_list
    for question_id in all_questions_id_list_random:
        question = all_questions.filter(id=question_id).first()
        quiz_taken_number_of_questions_dict = {"question": question}
        list_of_questions_generated_list.append(
            quiz_taken_number_of_questions_dict)
    
    # create QuizTaken object with all available information
    quiz_taken = QuizTaken(
        user=g.user,
        list_of_questions=list_of_questions_generated_list,
        number_of_questions=all_questions.count(),
        date_started=datetime.datetime.now(),
    )
    # save it
    quiz_taken.save()

    return quiz_taken

# registration form
class RegisterForm(Form):
    first_name = StringField(
        "First name", validators=[validators.Length(max=50)])
    last_name = StringField(
        "Last name", validators=[validators.Length(max=75)])
    email = StringField(
        "Email",
        validators=[
            validators.Email(message="Enter valid email"),
            validators.DataRequired(message="Email is required"),
        ],
    )
    username = StringField(
        "Username",
        validators=[
            validators.Length(min=10, max=150),
            validators.DataRequired(message="Username is required.")],
    )
    # password fields hold few validator as also qualTo which will compare 
    # value against `confirm_password` field
    #  in the case that the values are different it will print out the 
    # appropriate message which is set here
    password = PasswordField(
        "Password",
        validators=[
            validators.Length(min=10, max=45),
            validators.DataRequired(message="Password is required"),
            validators.EqualTo(
                fieldname="confirm_password", 
                message="Entered passwords do not match"),
        ],
    )
    # confirm password field, which should be the same as the password field
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[validators.Length(min=10, max=45), validators.DataRequired(
            "Confirm password is required.")],
    )

# login form
class LoginForm(Form):
    username = StringField(
        "Username",
        validators=[
            validators.Length(min=10, max=150),
            validators.DataRequired(message="Username is required")],
    )
    password = StringField(
        "Password",
        validators=[
            validators.Length(min=10, max=45), 
            validators.DataRequired(message="Password is required.")],
    )


# defining route for register
@app.route("/register/", methods=["GET", "POST"])
def register():
    #  init Registration form and add request.form data to it
    form = RegisterForm(request.form)
    #  at the POST request chck if the form is valid 
    # (if the initial validation is passed)
    if request.method == "POST" and form.validate():
        #  create a new user based on the form data, 
        # and also generate password hash
        # to store password as a hash instead of a plain string
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(
                orm.password.data, method="sha256"),
        )
        # save new user
        new_user.save()
        flash("Successfully registered", "success")
        # return success message that registration is done
        return jsonify({"registration": "done"})
    else:
        return render_template("register.html", form=form)

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        # this returns List and we need only one object and that
        # is why .first() is required
        user = User.objects(username=form.username.data).first()
        # if user exists
        if user:
            if check_password_hash(user.password, form.password.data):
                # add user data in session
                session["logged_in"] = True
                session["username"] = user.username
                return jsonify({"data": "User is logged in"})
            else:
                # Incorrect credentials - reload login and present form
                flash("Incorrect credentils", "Danger")
                return redirect(url_for("login"))

    # present form (on GET)
    return render_template("login.html", form=form)

@app.route("/", methods=["GET"]) 
def index():
    return render_template("index.html")

   
@app.route("/quiz/", methods=["GET", "POST"])
def quiz():
    # see if user is in global object - if not redirect to login
    if not g.user:
        return redirect(url_for("login"))

    # this is overall quiz with user history
    all_users_quizes = QuizTaken.objects(user=g.user)

    if request.method == "POST":
        quiz_id = request.form.get("quiz")
        # if no quiz_id, create a new quiz and redirect to quiz start
        if quiz_id is None or quiz_id == "0":
            #  create user quiz via helper function
            user_quiz = create_user_quiz()
            return redirect(url_for("quiz_start", quiz_id=user_quiz.id))

        #  open specific quiz with the specific ID
        return redirect(url_for("quiz_start", quiz_id=quiz_id))

    # get last unfinished quiz - to connect it with  a submit option 
    # `Continue` in template
    last_unfinished_quiz = all_users_quizes.filter(is_done=False).first()

    # display all of the previous users quizes
    return render_template(
        "quiz_overview.html", 
        user=g.user, users_quizes=all_users_quizes, 
        last_unfinished_quiz=last_unfinished_quiz
    )
