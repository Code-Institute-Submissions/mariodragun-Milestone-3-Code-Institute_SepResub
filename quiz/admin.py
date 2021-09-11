from flask_admin.base import Admin, AdminIndexView, expose
from flask_admin.contrib.mongoengine.view import ModelView
from .models import User, Question, QuizTaken
from flask import g
from flask_admin.menu import MenuLink


# defining User Admin View which we will use on the Admin site of the Flask app
class UserAdminView(ModelView):
    column_filters = ["username", "email"]


# defining QuestionAdminView which we will use
class QuestionsAdminView(ModelView):
    column_filters = ["title"]


class QuizTakenAdminView(ModelView):
    column_filter = ["user"]


class AdminDashboardView(AdminIndexView):

    # define if element is visible - will remove the first Home button
    def is_visible(self):
        return False

    @expose("/")
    def index(self):
        # check if the user has the permission to access this page, only
        # admin users should be able to see admin panel
        if g.user and g.user.is_admin:
            return self.render("admin/index.html")
        # return redirect(url_for("login"))
        return self.render("common/error_view_403.html")


def register_admin_views(app):
    """
    Initialize admin views and register all the views which are
    required here.
    """

    # create admin instance usign new Admin index view
    admin = Admin(
        app, index_view=AdminDashboardView(), template_mode="bootstrap4"
    )

    # add views to the Admin
    admin.add_view(UserAdminView(User))
    admin.add_view(QuestionsAdminView(Question))
    admin.add_view(QuizTakenAdminView(QuizTaken))

    # define link to the Website, to be able to return back to Quiz
    admin.add_link(MenuLink(name="Back to the Website", category="", url="/"))
