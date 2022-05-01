from flask import Blueprint, render_template

men = Blueprint('men', __name__)


@men.route('/men')
def index():
    params = {
        "logined": True
    }
    return render_template('men.html', **params)
