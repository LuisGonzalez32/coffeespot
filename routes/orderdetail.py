from utils.db import db


class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(50), nullable=True)
    unitCost = db.Column(db.Integer, nullable=False)
    totalCost = db.Column(db.Integer, nullable=False)

    def __init__(self, orderId, quantity, description, unitCost, totalCost) -> None:
        self.orderId = orderId
        self.quantity = quantity
        self.description = description
        self.unitCost = unitCost
        self.totalCost = totalCost

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.orderId}, '{self.quantity}', '{self.description}', '{self.unitCost}', '{self.totalCost}')"
