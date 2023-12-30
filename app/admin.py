from flask_admin import Admin
from wtforms import SelectField, TextAreaField

from app import app, db
from flask_admin.contrib.sqla import ModelView,form
from app.models import Category, Product


admin = Admin(app=app, name='Quản Trị Bán Hàng', template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active', 'category']
    column_hide_backrefs = False
    with app.app_context():
        cate_choices = Category.query.filter(Category.name)



admin.add_view(ModelView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))