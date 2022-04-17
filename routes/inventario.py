from flask import Blueprint, render_template, redirect, url_for
from forms.inventarioCreateForms import inventarioCreateForm
from forms.inventarioUpdateForms import inventarioUpdateForm
from models.inventario import Inventarios
from utils.db import db

Inventario = Blueprint("Inventario", __name__, url_prefix="/Inventario")



@Inventario.route("/")
def home():
    return render_template("Inventario/home.html")
    
    
@Inventario.route("/create", methods=["GET", "POST"])
def create():
    form = inventarioCreateForm()
    if form.validate_on_submit():
        productId = form.productId.data
        code = form.code.data
        description = form.description.data
        price = form.price.data
        stock = form.stock.data
        newInventario = Inventarios(productId, code, description, price, stock)
        db.session.add(newInventario)
        db.session.commit()
        return redirect(url_for("Inventario.home"))
    return render_template("Inventario/create.html", form=form)


@Inventario.route("/inventario", methods=["GET", "POST"])
def inventario():
    invent = Inventarios.query.all()
    return render_template("Inventario/inventario.html", invent=invent)

@Inventario.route("/update/<int:inventarioId>", methods=["GET", "POST"])
def update(inventarioId):
    currentInventario = Inventarios.query.filter_by(id=inventarioId).first()
    form = inventarioUpdateForm()
    if form.validate_on_submit():
        productId = form.productId.data
        code = form.code.data
        description = form.description.data
        price = form.price.data
        stock = form.stock.data
        currentInventario.productId = productId
        currentInventario.code = code
        currentInventario.description = description
        currentInventario.price = price
        currentInventario.stock = stock
        db.session.add(currentInventario)
        db.session.commit()
        return redirect(url_for("Inventario.inventario"))
    return render_template("Inventario/update.html",form=form, inventarioId=currentInventario)


@Inventario.route("/delete/<int:inventarioId>")
def delete(inventarioId):
    currentInventario = Inventarios.query.filter_by(id=inventarioId).first()
    db.session.delete(currentInventario)
    db.session.commit()
    return redirect(url_for("Inventario.inventario"))