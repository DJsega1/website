from flask import Blueprint, render_template
from ..models import *

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin_panel():
    params = {
        "title": "Панель администратора",
        "brand_list": Brand.query.all(),
        "material_list": Material.query.all(),
        "color_list": Color.query.all(),
        "type_list": Type.query.all(),
        "sex_list": Sex.query.all()
    }
    return render_template('admin_panel.html', **params)
