from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a6ffe27dfffdee4138f79a9dc7f5619c'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy()
db.init_app(app)

from website.blueprints.main import main as main_blueprint
app.register_blueprint(main_blueprint)
from website.blueprints.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from website.blueprints.shop import shop as shop_blueprint
app.register_blueprint(shop_blueprint)

import website.views
import website.models

db.create_all(app=app)
