from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=20),
        ],
        render_kw={"placeholder": "username"},
    )

    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=4, max=20),
        ],
        render_kw={"placeholder": "password"},
    )

    submit = SubmitField("register")

    def validate_username(self, username):
        currentUser = User.query.filter_by(username=username).first()
        if currentUser:
            raise ValidationError("the username already exists")
