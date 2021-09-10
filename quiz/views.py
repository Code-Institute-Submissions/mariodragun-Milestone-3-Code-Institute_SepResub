from .forms import RegisterForm, LoginForm
from flask import session, request, flash, redirect, render_template, url_for
from flask import current_app as app
from .models import User, QuizTaken
from werkzeug.security import check_password_hash, generate_password_hash
from .helpers import create_user_quiz, set_users_questions


@app.route("/register/", methods=["GET", "POST"])
def register():
    #  init Registration form and add request.form data to it
    form = RegisterForm(request.form)
    # at the POST request chck if the form is valid
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
            password=generate_password_hash(form.password.data, method="sha256"),
        )
        # save new user
        new_user.save()
        flash("Successfully registered", "success")
        # return success message that registration is done
        return redirect(url_for("login"))
    else:
        return render_template("register.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        # this returns List and we need only one object and that
        # is why .first() is required
        user = User.objects(username=form.username.data).first()
        # if user exists
        if user:
            if check_password_hash(user.password, form.password.data):
                # add user data in session
                session["logged_in"] = True
                session["username"] = user.username
                user_id = user.id
                session["user_id"] = str(user_id)
                return redirect(url_for("quiz"))
            else:
                # Incorrect credentials - reload login and present form
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

    # get last unfinished quiz - to connect it with a submit option
    # Continue` in template
    last_unfinished_quiz = all_users_quizes.filter(is_done=False).first()

    # display all of the previous users quizes
    return render_template(
        "quiz_overview.html", user=g.user, users_quizes=all_users_quizes, last_unfinished_quiz=last_unfinished_quiz
    )


# create quiz route with `quiz_id`
@app.route("/quiz/<quiz_id>", methods=["GET", "POST"])
def quiz_start(quiz_id):
    """View to start a quiz"""

    #  if not user in global object - redirect to login
    if not g.user:
        return redirect(url_for("login"))

    # get the existing quiz object form the user - based on the quiz_id
    existing_quiz = QuizTaken.objects(user=g.user, id=quiz_id).first()
    # if exsting quiz is done redirect to quiz end
    if existing_quiz.is_done:
        return redirect(url_for("quiz_end", quiz_id=quiz_id))

    if request.method == "POST":
        question_id = request.form.get("q")
        supplied_answer = request.form.getlist("q_answers")[0]

        users_quiz = existing_quiz
        users_quiz__list_of_questions = users_quiz.list_of_questions
        for list_of_q in users_quiz__list_of_questions:

            # find question which corresponds with the id
            # supplied from the form
            if str(list_of_q.question.id) == str(question_id):
                # assing that question to be our question
                question = list_of_q.question
                correct_answer = None
                # iter through questions answers
                for answer in question.answers:
                    if answer.is_correct:
                        correct_answer = answer

                list_of_q.chosen_answer = supplied_answer

                #  check if supplied answer is the correct one
                if correct_answer.answer == supplied_answer:
                    list_of_q.is_correct = True
                    users_quiz.correct_answers = int(users_quiz.correct_answers) + 1

        # update quiz object
        users_quiz.save()

        return redirect(url_for("quiz_start", quiz_id=quiz_id))

    else:
        question = set_users_questions(existing_quiz=existing_quiz)
        if question is None:
            return redirect(url_for("quiz_end", quiz_id=quiz_id))

        return render_template("quiz.html", question=question, quiz_id=quiz_id)


@app.route("/quiz/<quiz_id>/completed", methods=["GET"])
def quiz_end(quiz_id):
    if not g.user:
        return redirect(url_for("login"))

    existing_quiz = QuizTaken.objects(user=g.user, id=quiz_id).first()
    if not existing_quiz.is_done:
        return redirect(url_for("quiz_start", quiz_id=quiz_id))

    return render_template("quiz_completed.html", user=g.user, score=existing_quiz.overall_score)
