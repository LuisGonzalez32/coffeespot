from utils.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    rank = db.Column(db.String(15), nullable=False)

    def __init__(self, username, password, status="active", rank="admin") -> None:
        self.username = username
        self.password = password
        self.status = status
        self.rank = rank

    def __repr__(self) -> str:
        return f"User({self.id}, {self.username}, '{self.password}', '{self.status}', '{self.rank}'"
