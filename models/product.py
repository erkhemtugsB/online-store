from models import db  # ✅ Import from models, not a new instance

class Product(db.Model):
    __tablename__ = 'product'  # ✅ Ensure table names are explicit
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
