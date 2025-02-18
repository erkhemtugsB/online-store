from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Dummy user data for authentication
users = {
    'test': 'test'
}

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please login first!', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))
# Add new product
@app.route('/newproduct', methods=['POST'])
def newproduct():
    name = request.form['product-name']
    price = request.form['product-price']
    description = request.form['product-description']
    image = request.files['product-image']
    image_filename = image.filename
    image.save(f'static/assets/products/{image_filename}')

    new_product = Product(name=name, price=price, description=description, image=image_filename)
    db.session.add(new_product)
    db.session.commit()

    flash('Product added successfully!', 'success')
    return redirect(url_for('dashboard'))

# Get all products
@app.route('/api/products', methods=['GET'])
def api_get_products():
    products = Product.query.all()
    products_list = [{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'image': product.image
    } for product in products]
    return {'products': products_list}

# Get a specific product by ID
@app.route('/api/products/<int:id>', methods=['GET'])
def api_get_product(id):
    product = Product.query.get(id)
    if product:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'image': product.image
        }
        return product_data
    else:
        return {'message': 'Product not found'}, 404



# Delete product
@app.route('/api/products/delete/<int:id>', methods=['DELETE'])
def api_delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return {'message': 'Product deleted successfully!'}



@app.route('/order', methods=['GET', 'POST'])
def order():

    return render_template('product.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)