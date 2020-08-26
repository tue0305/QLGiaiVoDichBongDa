from flask import render_template

from app import app, models


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/inner-page')
def inner_page():
    return render_template('inner-page.html')

@app.route('/model')
def model():
    models.db.create_all()
    return 'successful'

if __name__ == "__main__":
    app.run(debug=True)
