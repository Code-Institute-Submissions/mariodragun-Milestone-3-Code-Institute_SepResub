from flask_admin.base import Admin
from flask_admin.contrib.mongoengine.view import ModelView
from .models import User, Question, QuizTaken


# defining User Admin View which we will use on the Admin site of the Flask app
class UserAdminView(ModelView):
    column_filters = ["username", "email"]


# defining QuestionAdminView which we will use
class QuestionsAdminView(ModelView):
    column_filters = ["title"]


class QuizTakenAdminView(ModelView):
    column_filter = ["user"]


def register_admin_views(app):
    """Initialize admin views and register all the views which are required here."""

    admin = Admin(app, name="Quiz", template_mode="bootstrap3")

    # add views to the Admin
    admin.add_view(UserAdminView(User))
    admin.add_view(QuestionsAdminView(Question))
    admin.add_view(QuizTakenAdminView(QuizTaken))
