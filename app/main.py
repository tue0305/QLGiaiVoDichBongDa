from flask import render_template, request, session, redirect, url_for

from functools import wraps

from app import app, models, dao

def login_required(f):
    @wraps(f)
    def check(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return check

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/inner-page')
def inner_page():
    return render_template('inner-page.html')

# @app.route('/model')
# def model():
#     models.db.create_all()
#     return 'successful'



@app.route("/login", methods=["GET", "POST"])
def login():
    err_msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.validate_user(username=username, password=password)
        if user:
            # session["user"] =  user
            # if "next" in request.args:
            #     return redirect(request.args["next"])
            return redirect('/admin')
        else:
            err_msg = "Đăng nhập không thành công"
    return render_template("login.html", err_msg=err_msg)

@app.route("/logout")
def logout():
    del session["user"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
