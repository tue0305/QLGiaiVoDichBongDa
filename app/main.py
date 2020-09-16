from functools import wraps

from flask import redirect, render_template, request, session, url_for
from flask_login import login_user

from app import app, dao, login, models
from app.models import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/tournament')
def tournament():
    return render_template('tournament.html', tournaments=dao.read_tournament())

@app.route('/team')
def team():
    return render_template('team.html', teams=dao.read_team())

@app.route('/player')
def player():
    return render_template('player.html', players=dao.read_player())

@app.route('/login-user', methods=['GET', 'POST'])
def login_users():
    return render_template('login.html')

@app.route('/register-user', methods=['POST'])
def register_users():
    return ''

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.validate_user(username=username, password=password)
        if user:
            login_user(user=user)
    return redirect('/admin')

@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)

@app.route('/model')
def model():
    models.db.create_all()
    return 'successful'

if __name__ == "__main__":
    app.run(debug=True)
