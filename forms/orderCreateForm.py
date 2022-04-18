from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from models.user import User


class OrderCreateForm(FlaskForm):
    buyer = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "buyer"},
    )

    provider = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=20),
        ],
        render_kw={"placeholder": "provider"},
    )

    orderCode = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "order code"},
    )

    saleCode = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "sale code"},
    )

    submit = SubmitField("create")