from flask import Blueprint, render_template, request, make_response
from flask import redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from website import db
from website import app
from website.forms import RegisterForm, LoginForm
from website.utils.additional_functions import no_cache
import uuid


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    reg_data = RegisterForm(request.form)
    if not reg_data.validate_on_submit():
        return render_template("signup.html", form=reg_data)
    first_name, last_name, email = reg_data.first_name.data, reg_data.last_name.data, reg_data.email.data
    address, postcode, cart = reg_data.address.data, reg_data.postcode.data, reg_data.cart.data
    password = reg_data.password.data
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
    auth_data = LoginForm(request.form)
    if not auth_data.validate_on_submit():
        return render_template("login.html", form=auth_data, errors=[])
    email = auth_data.email.data
    password = auth_data.password.data
    remember = auth_data.remember.data
    user = User.query.filter_by(email=email).first()
    if user:
        user_password_hash = user.password
        if check_password_hash(user_password_hash, password):
            login_user(user, remember=remember)
            return redirect(url_for("main.index"), 301)
    return render_template("login.html", form=auth_data, errors=["Login or password are incorrect"])


@auth.route("/logout")
@no_cache
def logout():
    logout_user()
    resp = redirect(url_for("main.index"), 301)
    return resp
