from flask import Blueprint, render_template, request, make_response
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from website import db
from website import app
from functools import wraps
from datetime import datetime, timedelta
import uuid
import jwt

auth = Blueprint('auth', __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("SESSION_TOKEN")
        if not token:
            return make_response("Token is missing", 401)
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(public_id=data["public_id"]).first()
            if not current_user:
                return make_response("Invalid token", 401)
            is_admin = data["is_admin"]
        except Exception:
            return make_response("Invalid token", 401)
        return f((current_user, is_admin), *args, **kwargs)
    return decorated()


@auth.route('/signup')
def signup_page():
    return render_template("signup.html")


@auth.route('/signup', methods=['POST'])
def signup():
    reg_data = request.form
    first_name, last_name, email = reg_data.get("first_name"), reg_data.get("last_name"), reg_data.get("email")
    address, postcode, cart = reg_data.get("address"), reg_data.get("postcode"), reg_data.get("cart")
    password = reg_data.get("password")
    if not User.query.filter_by(email=email).first():
        user = User(public_id=str((uuid.uuid4())),
                    email=email,
                    password=generate_password_hash(password),
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    postcode=int(postcode),
                    cart=cart)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"), 301)
    else:
        return make_response("User already exist", 202)


@auth.route("/login")
def login_page():
    return render_template("login.html")


@auth.route('/login', methods=['POST', 'GET'])
def login():
    auth_data = request.form
    email = auth_data.get('email')
    password = auth_data.get('password')
    remember = True if auth_data.get("remember") else False
    if not auth_data or not email or not password:
        return make_response("Some fields are clear", 401)
    user = User.query.filter_by(email=email).first()
    if not user:
        return make_response("Invalid password or login", 401)
    user_password_hash = user.password
    if not check_password_hash(user_password_hash, password):
        return make_response("Invalid password or login", 401)
    jwt_token = jwt.encode({'public_id': user.public_id,
                            'exp': datetime.utcnow() + timedelta(minutes=30),
                            'is_admin': (user.public_id == 0)},
                           app.config["SECRET_KEY"])
    resp = make_response(redirect(url_for("main.index"), 301))
    resp.set_cookie("SESSION_TOKEN", jwt_token, expires=30)
    return resp


@auth.route("/logout")
def logout(user):
    resp = make_response(redirect(url_for("main.index"), 302))
    resp.set_cookie('SESSION_TOKEN', '', expires=0)
    return resp
