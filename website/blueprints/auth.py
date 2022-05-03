from flask import Blueprint, render_template, request, make_response
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from website import db
from website import app
import uuid


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
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
        login_user()
        return redirect(url_for("main.index"), 301)
    else:
        return make_response("User already exist", 202)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
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
    login_user(user)
    resp = redirect(url_for("main.index"), 301)
    return resp


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"), 301)
