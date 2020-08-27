import os
import hashlib

from app import app
from app.models import *


#kiểm tra login




def validate_user(username, password):
    
    # password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
    user = None
    user = User.query.filter(User.UserName == username.strip(), User.PassWord == password.strip()).first()
    return user