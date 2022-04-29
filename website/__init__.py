from flask import Flask
app = Flask(__name__)

from website.blueprints.main import main as main_blueprint
app.register_blueprint(main_blueprint)
from website.blueprints.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

import website.views
