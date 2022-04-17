from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class inventarioCreateForm(FlaskForm):
    productId = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "ID del producto"},
    )

    code = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Codigo del producto"},
    )

    description = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Descripcion"},
    )
    
    price = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Precio"},
    )
    
    stock = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Stock"},
    )

    submit = SubmitField("create task")