from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "b'\xdc\xec\xe5\xa393\xba\x0e\xf3\xe7\x8d-A\x1c6\xae'"

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:8774165@localhost/qlgiaibd?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name='FOOTBALL LEAGUE', template_mode='bootstrap3')

login = LoginManager(app=app)
