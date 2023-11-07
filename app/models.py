from app import db, app
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(200), default="https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/anh-chup-man-hinh-2022-09-08-luc-01-59-18-removebg-preview.png")
    active = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        #c1 = Category(name='Mobile')
        #c2 = Category(name='Tablet')
        #c3 = Category(name='Desktop')

        #db.session.add(c1)
        #db.session.add(c2)
        #db.session.add(c3)

        #db.session.commit()

        p1 = Product(name='iPhone 13', price=22000000, category_id=1)
        p2 = Product(name='Galaxy Tab S9', price=28000000, category_id=2)
        p3 = Product(name='iPad Pro 2023', price=21000000, category_id=2)
        p4 = Product(name='Galaxy S23', price=18000000, category_id=1)
        p5 = Product(name='iPhone 15', price=22000000, category_id=1)

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()