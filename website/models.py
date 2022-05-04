from website import db
from flask_login import UserMixin
from website import login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    public_id = db.Column(db.String(50), unique=True)
    is_admin = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    postcode = db.Column(db.Integer)
    cart = db.Column(db.String)


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    brand = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.brand


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    type = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.type


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    material = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.material


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    color = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.color


class Sex(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    sex = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.sex


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                   unique=True, nullable=False)
    size = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.size


class Item(db.Model):
    article = db.Column(db.Integer, primary_key=True, autoincrement=True,
                        unique=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String)
    brand = db.Column(db.String(100), db.ForeignKey('brand.id'), nullable=False)
    type = db.Column(db.String(100), db.ForeignKey('type.id'), nullable=False)
    material = db.Column(db.String(100), db.ForeignKey('material.id'), nullable=False)
    color = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    sex = db.Column(db.Integer, db.ForeignKey('sex.id'), nullable=False)
    size = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


@login_manager.user_loader
def load_user(public_id):
    return User.query.get(public_id)
