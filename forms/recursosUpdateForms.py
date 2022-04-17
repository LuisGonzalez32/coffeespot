from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length


class recursosUpdateForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "username"},
    )

    password = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "password"},
    )


    submit = SubmitField("Actualizar usuario")