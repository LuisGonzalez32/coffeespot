from utils.db import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    rank = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, status, rank) -> None:
        self.username = username
        self.password = password
        self.status = status
        self.rank = rank

    def __repr__(self):
        return f"User({self.id}, '{self.username}', '{self.password}', '{self.status}', '{self.rank}')"
