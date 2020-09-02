import hashlib
import os

from app import app
from app.models import *


def validate_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.userName == username.strip(), 
                            User.passWord == password).first()
