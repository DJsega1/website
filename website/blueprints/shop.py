from flask import Blueprint, render_template, request
from ..models import *

shop = Blueprint('shop', __name__)


@shop.route('/men', methods=['GET', 'POST'])
def men():
    items = Item.query.filter(Item.sex == 1).all()
    params = {
        "title": "Мужская одежда",
        "brand_list": Brand.query.all(),
        "material_list": Material.query.all(),
        "color_list": Color.query.all(),
        "type_list": Type.query.all(),
        "logined": True
    }
    if request.method == "POST":
        print(request.form)
    return render_template('shop.html', **params)


@shop.route('/women')
def women():
    items = Item.query.filter(Item.sex == 2).all()
    params = {
        "title": "Женская одежда",
        "logined": True
    }
    if request.method == "POST":
        print(request.form)
    return render_template('shop.html', **params)


@shop.route('/kids')
def kids():
    items = Item.query.filter(Item.sex == 3).all()
    params = {
        "title": "Детская одежда",
        "logined": True
    }
    if request.method == "POST":
        print(request.form)
    return render_template('shop.html', **params)
