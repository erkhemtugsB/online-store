from flask import Blueprint, request, jsonify, redirect, url_for, flash, render_template
from app import db
from models.product import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/product')
def product():
    return render_template('product.html')

@products_bp.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'image': product.image
    } for product in products]
    return jsonify({'products': products_list})

@products_bp.route('/api/products/<int:id>', methods=['GET'])
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


@products_bp.route('/api/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully!'})
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/newproduct', methods=['POST'])
def new_product():
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
    return redirect(url_for('main.dashboard'))
