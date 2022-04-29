from flask import Blueprint, render_template

main = Blueprint('main', __name__)

print(__name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    return "Profile!"
#############
## https://flask-russian-docs.readthedocs.io/ru/latest/patterns/packages.html
#############

