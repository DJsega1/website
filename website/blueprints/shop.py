from flask import Blueprint, render_template
from website.models import *

shop = Blueprint('shop', __name__)


@shop.route('/men')
def men():
    items = Item.query.filter(Item.sex == 1).all()
    params = {
        "title": "Мужская одежда",
        "logined": True
    }
    return render_template('shop.html', **params)


@shop.route('/women')
def women():
    items = Item.query.filter(Item.sex == 2).all()
    params = {
        "title": "Женская одежда",
        "logined": True
    }
    return render_template('shop.html', **params)


@shop.route('/kids')
def kids():
    items = Item.query.filter(Item.sex == 3).all()
    params = {
        "title": "Детская одежда",
        "logined": True
    }
    return render_template('shop.html', **params)
