from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_admin import Admin
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:8774165@localhost/qlbongda?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

admin = Admin(app=app)