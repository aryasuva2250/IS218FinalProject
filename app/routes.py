"""Route declaration."""
from flask import current_app as app
from flask import render_template


@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]
    return render_template(
        'home.html',
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )

from flask import (
    Flask,
    url_for,
    render_template,
    redirect
)
from .forms import ContactForm


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )