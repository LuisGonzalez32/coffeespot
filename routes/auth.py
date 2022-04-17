from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from utils.bcryptService import bcrypt
from models.user import User
from utils.db import db

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        currentUser = User.query.filter_by(username=username).first()
        if currentUser:
            if bcrypt.check_password_hash(currentUser.password, password):
                login_user(currentUser)
            return redirect(url_for("auth.finanzas"))
    return render_template("login.html", form=form)

@auth.route("/")
@login_required
def finanzas():
    userList = None
    if "admin" in current_user.rank:
        # es un admin
        userList = User.query.all()
    else:
        # es un user
        userList = list((User.query.filter_by(id=current_user.id).first(),))
    return render_template("RRHH/home.html", user=current_user, userList=userList)


@auth.route("/cose", methods=["GET", "POST"])
def cose():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password)
        newUser = User(username, hashed_password, "active", "user")
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("cose.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/About")
def About():
    return render_template("Pagina/About.html")

@auth.route("/register")
def register():
    return render_template("register.html")


@auth.route("/Bebidas")
def Bebidas():
    return render_template("Pagina/Bebidas.html")

@auth.route("/BebidasCaliente")
def BebidasCaliente():
    return render_template("Pagina/BebidasCaliente.html")

@auth.route("/BebidasFrias")
def BebidasFrias():
    return render_template("Pagina/BebidasFrias.html")

@auth.route("/Contactos")
def Contactos():
    return render_template("Pagina/Contactos.html")

@auth.route("/Postres")
def Postres():
    return render_template("Pagina/Postres.html")

@auth.route("/Promociones")
def promociones():
    return render_template("Pagina/Promociones.html")



