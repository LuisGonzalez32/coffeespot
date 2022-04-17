from utils.db import db


class Inventarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __init__(self, productId, code, description, price, stock) -> None:
        self.productId = productId
        self.code = code
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self) -> str:
        return f"Inventario({self.id}, {self.productId}, '{self.description}', '{self.code}', '{self.price}','{self.stock}')"