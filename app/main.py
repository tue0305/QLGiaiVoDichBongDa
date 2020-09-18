from functools import wraps
from flask import redirect, render_template, request, session, url_for
from flask_login import login_user, current_user, logout_user

from app import app, dao, login, models
from app.models import *


def login_required(f):
    @wraps(f)
    def check(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("login_users", next=request.url))
        return f(*args, **kwargs)
    return check


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
    msg_err = ""
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.validate_user(username, password)
        if user:
            login_user(user=user)
            return redirect('/')
        else:
            msg_err = "Đăng nhập không thành công"

    return render_template('login.html', msg_err=msg_err)

@app.route('/logout-user')
def logout_users():
    logout_user()
    return redirect('/')

@app.route('/register-user', methods=['POST', 'GET'])
def register_users():
    if request.method == 'POST':
        msg_err = ""
        name = request.form.get('name').strip()
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        confirm = request.form.get('confirm-password').strip()
        email = request.form.get('email').strip()

        if password == confirm:
            dao.create_user(name=name, username=username, password=password, email=email)
        else:
            msg_err = "Đăng ký không thành công"
        return render_template('login.html', msg_err=msg_err)

@app.route('/contact')
def contact():
    return render_template('contact.html') 
    
@app.route('/create-tournament', methods=['GET', 'POST'])
@login_required
def create_tournament():
    if request.method == 'POST':
        name = request.form.get('name')
        from_date = request.form.get('from-date')
        to_date = request.form.get('to-date')
        avatar = request.form.get('avatar')

        dao.create_tournament(name, from_date, to_date, avatar)
        return redirect(url_for('tournament'))

    return render_template('create-tournament.html')


@app.route('/create-round', methods=['GET', 'POST'])
@login_required
def create_round():
    if request.method == 'POST':
        name = request.form.get('name')
        dao.create_round(name)

    return render_template('create-round.html')


@app.route('/create-team', methods=['GET', 'POST'])
@login_required
def create_team():
    if request.method == 'POST':
        name = request.form.get('name')
        home_yard = request.form.get('home-yard')
        count = request.form.get('count')
        avatar = request.form.get('avatar')

        dao.create_team(name, home_yard, count, avatar)

    return render_template('create-team.html')


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

# @app.route('/model')
# def model():
#     models.db.create_all()
#     return 'successful'

if __name__ == "__main__":
    app.run(debug=True)
