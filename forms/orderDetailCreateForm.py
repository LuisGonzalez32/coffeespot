from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length


class OrderDetailCreateForm(FlaskForm):
    orderId = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "orderId..."},
    )

    quantity = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "quantity..."},
    )

    description = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=50),
        ],
        render_kw={"placeholder": "description..."},
    )

    unitCost = IntegerField(
        validators=[
            InputRequired(),
        ],
        render_kw={"placeholder": "unit cost..."},
    )

    submit = SubmitField("create")
