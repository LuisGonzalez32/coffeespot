from utils.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
 

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self) -> str:
        return f"Recursos({self.id}, {self.username}, '{self.password}'"