from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from forms.orderDetailCreateForm import OrderDetailCreateForm
from utils.db import db
from models.order import Order
from models.orderdetail import OrderDetail

orderDetails = Blueprint("orderDetails", __name__, url_prefix="/orderDetails")


@orderDetails.route("/")
@login_required
def home():
    return render_template("Finanzas/detailHome.html", user=current_user)


@orderDetails.route("/<int:orderId>")
@login_required
def homeByOrderId(orderId):
    currentOrder = Order.query.filter_by(id=orderId).first()
    orderDetailList = OrderDetail.query.filter_by(orderId=orderId).all()
    return render_template("Finanzas/detailHome.html", order=currentOrder, user=current_user, items=orderDetailList)


@orderDetails.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrderDetailCreateForm()
    if form.validate_on_submit():
        orderId = form.orderId.data
        currentOrder = Order.query.filter_by(id=orderId).first()

        quantity = form.quantity.data
        description = form.description.data
        unitCost = form.unitCost.data
        totalCost = quantity * unitCost
        currentOrder.totalSale += totalCost

        newOrderDetail = OrderDetail(orderId, quantity, description, unitCost, totalCost)
        db.session.add(newOrderDetail)
        db.session.add(currentOrder)
        db.session.commit()
        return redirect(url_for("Finanzas.detailHome"))
    return render_template("Finanzas/detailCreate.html", form=form)


@orderDetails.route("/create/<int:orderId>", methods=["GET", "POST"])
@login_required
def createByOrderId(orderId):
    form = OrderDetailCreateForm(orderId=orderId)
    if form.validate_on_submit():
        currentOrder = Order.query.filter_by(id=orderId).first()

        quantity = form.quantity.data
        description = form.description.data
        unitCost = form.unitCost.data
        totalCost = quantity * unitCost
        currentOrder.totalSale += totalCost

        newOrderDetail = OrderDetail(orderId, quantity, description, unitCost, totalCost)
        db.session.add(newOrderDetail)
        db.session.add(currentOrder)
        db.session.commit()
        return redirect(url_for("orderDetails.homeByOrderId", orderId=orderId))
    return render_template("Finanzas/detailCreate.html", form=form, user=current_user, orderId=orderId)
