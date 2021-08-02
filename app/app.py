'''
from flask import Flask, render_template, make_response, redirect, url_for


app = Flask(__name__)
app.config.from_object('config.Config')
# Using a production configuration
app.config.from_object('config.ProdConfig')
# Using a development configuration
app.config.from_object('config.DevConfig')

@app.route("/")
def home():
    """Serve homepage template."""
    return render_template(
        'index.html',
        title='Flask-Login Tutorial.',
        body="You are now logged in!"
    )
@app.route("/api/v2/test_response")
def users():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        headers=headers
    )

@app.route("/login")
def login():
    return redirect(url_for('dashboard'))
'''