from flask_admin import Admin, BaseView, expose
from app import app, db
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, UserRoleEnum
from flask_login import logout_user, current_user
from flask import redirect


admin = Admin(app=app, name='Quản Trị Bán Hàng', template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return  current_user.is_authenticated


class MyProductView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'price', 'active', 'category']
    column_hide_backrefs = False
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    can_export = True
    edit_modal = True

    with app.app_context():
        cate_choices = Category.query.filter(Category.name)


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(LogoutView(name='Đăng xuất'))