from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth
from routes.recursos import Recursos
from routes.inventario import Inventario
from routes.orders import orders
from routes.orderdetails import orderDetails
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from utils.loginManagerService import login_manager
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

app.register_blueprint(auth)
app.register_blueprint(Recursos)
app.register_blueprint(Inventario)
app.register_blueprint(orders)
app.register_blueprint(orderDetails)

