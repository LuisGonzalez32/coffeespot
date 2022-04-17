from flask import Blueprint, render_template, redirect, url_for
from forms.recursosCreateForms import recursosCreateForm
from forms.recursosUpdateForms import recursosUpdateForm
from utils.bcryptService import bcrypt
from models.user import User
from utils.db import db

Recursos = Blueprint("Recursos", __name__, url_prefix="/Recursos")



@Recursos.route("/")
def home():
    return render_template("RRHH/home.html")


@Recursos.route("/create", methods=["GET", "POST"])
def create():
    form = recursosCreateForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password)
        newRecursos = User(username, hashed_password)
        db.session.add(newRecursos)
        db.session.commit()
        return redirect(url_for("RRHH/Recursos.home"))
    return render_template("RRHH/create.html", form=form)


@Recursos.route("/recursos", methods=["GET", "POST"])
def recursos():
    recursos = User.query.all()
    return render_template("RRHH/recursos.html", recursos=recursos)


@Recursos.route("/update/<int:RecursosId>", methods=["GET", "POST"])
def update(RecursosId):
    currentRecursos = User.query.filter_by(id=RecursosId).first()
    form = recursosUpdateForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password)
        currentRecursos.username = username
        currentRecursos.password = hashed_password
        db.session.add(currentRecursos)
        db.session.commit()
        return redirect(url_for("Recursos.recursos"))
    return render_template("RRHH/update.html",form=form, RecursosId=currentRecursos)


@Recursos.route("/delete/<int:RecursosId>")
def delete(RecursosId):
    currentRecursos = User.query.filter_by(id=RecursosId).first()
    db.session.delete(currentRecursos)
    db.session.commit()
    return redirect(url_for("Recursos.recursos"))