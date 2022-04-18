from utils.db import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer = db.Column(db.String(50), nullable=False)
    provider = db.Column(db.String(50), nullable=False)
    totalSale = db.Column(db.Integer, nullable=False)
    orderCode = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=True)
    saleCode = db.Column(db.Integer, nullable=False)

    def __init__(self, buyer, provider, orderCode, saleCode, totalSale=0, date=None) -> None:
        self.buyer = buyer
        self.provider = provider
        self.orderCode = orderCode
        self.saleCode = saleCode
        self.totalSale = totalSale
        self.date = date

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.buyer}, '{self.provider}', '{self.totalSale}', '{self.orderCode}', '{self.date}', '{self.saleCode}')"
