from flask import Blueprint, render_template, session, redirect, url_for, request
from flask_login import login_required, current_user
from website.models import *
from website.utils.additional_functions import no_cache
from website.forms import AdminForm

admin = Blueprint('admin', __name__)


@login_required
@no_cache
@admin.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    user = User.query.filter_by(public_id=session["public_id"]).first()
    if not user or not user.is_admin:
        return redirect(url_for("main.profile"))
    item_form = AdminForm(request.form)
    params = {
        "success": False,
        "form": item_form,
        "errors": [],
        "title": "Панель администратора",
        "brand_list": Brand.query.all(),
        "material_list": Material.query.all(),
        "color_list": Color.query.all(),
        "type_list": Type.query.all(),
        "sex_list": Sex.query.all()
    }
    if not item_form.validate_on_submit():
        print(item_form.form_errors)
        return render_template('admin_panel.html', **params)
    item = Item()
    item.article = item_form.vendor_code.data
    item.brand = item_form.brand.data
    item.name = item_form.name.data
    item.description = item_form.description.data
    item.amount = item_form.amount.data
    item.price = item_form.price.data
    item.color = item_form.color.data
    item.type = item_form.type.data
    item.material = item_form.material.data
    item.sex = item_form.sex.data
    path = f'static/img/{item.article}'
    if not os.path.isdir(path):
        os.mkdir(path)
    for image in item_form.pictures.data:
        image.save(os.path.join(path, image.filename))
    db.session.add(item)
    db.session.commit()
    params["success"] = True
    return render_template('admin_panel.html', **params)
