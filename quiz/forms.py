from wtforms import Form, StringField, PasswordField, validators


# registration form
class RegisterForm(Form):
    first_name = StringField(
        "First name", validators=[validators.Length(max=50)]
    )
    last_name = StringField(
        "Last name", validators=[validators.Length(max=75)]
    )
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
            validators.DataRequired(message="Username is required."),
        ],
    )
    # password fields hold few validator as also qualTo which will compare
    # value against `confirm_password` field
    # in the case that the values are different it will print out the
    # appropriate message which is set here
    password = PasswordField(
        "Password",
        validators=[
            validators.Length(min=10, max=45),
            validators.DataRequired(message="Password is required"),
            validators.EqualTo(
                fieldname="confirm_password",
                message="Entered passwords do not match",
            ),
        ],
    )
    # confirm password field, which should be the same as the password field
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            validators.Length(min=10, max=45),
            validators.DataRequired("Confirm password is required."),
        ],
    )


# login form
class LoginForm(Form):
    username = StringField(
        "Username",
        validators=[
            validators.Length(min=10, max=150),
            validators.DataRequired(message="Username is required"),
        ],
    )
    password = StringField(
        "Password",
        validators=[
            validators.Length(min=10, max=45),
            validators.DataRequired(message="Password is required."),
        ],
    )
