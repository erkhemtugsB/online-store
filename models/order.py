from models import db  # ✅ Import the same db instance
from models.product import Product  # ✅ Import Product after defining db

class Order(db.Model):
    __tablename__ = 'order'  # ✅ Explicit table name
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_address = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref=db.backref('orders', lazy=True))
