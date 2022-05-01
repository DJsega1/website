from flask import Blueprint, render_template

main = Blueprint('main', __name__)

print(__name__)


@main.route('/')
def index():
    # TODO: Добавить сессию пользователя
    params = {
        "logined": True
    }
    return render_template('index.html', **params)


@main.route('/profile')
def profile():
    return "Profile!"
