import hashlib
import os

from app import app, db
from app.models import *


def validate_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.userName == username.strip(), 
                            User.passWord == password).first()

def read_tournament():
    return Tournament.query.all()

def read_team():
    return Team.query.all()

def read_player():
    return Player.query.all()

def create_user(name, username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name, userName=username, passWord=password, email=email)
    db.session.add(user)
    db.session.commit()
    
def create_tournament(name, from_date, to_date, avatar):
    tournament = Tournament(tenGD=name, ngayBatDau=from_date, ngayKetThuc=to_date, avatar=avatar)
    db.session.add(tournament)
    db.session.commit()

def create_round(name):
    round = Round(tenVD=name)
    db.session.add(round)
    db.session.commit()


def create_team(name, home_yard, count, avatar):
    team = Team(tenDB=name, sanNha=home_yard, soLuongCauThu=count, avatar=avatar)
    db.session.add(team)
    db.session.commit()

