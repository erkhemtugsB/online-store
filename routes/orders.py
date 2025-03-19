from flask import Blueprint, request, jsonify, redirect, url_for, flash, render_template
from app import db
from models.order import Order
from models.product import Product

orders_bp = Blueprint('orders', __name__)


@orders_bp.route('/neworder', methods=['POST'])
def new_order():
   product_id = request.form['product_id']
   customer_name = request.form['customer_name']
   customer_address = request.form['customer_address']
   customer_phone = request.form['customer_phone']
   quantity = request.form['quantity']

   new_order = Order( product_id=product_id, customer_name=customer_name, customer_address=customer_address, customer_phone=customer_phone, quantity=quantity)
   db.session.add(new_order)
   db.session.commit()
   flash
   return redirect(url_for('products.product'))

@orders_bp.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    orders_list = [{
        'id': order.id,
        'product_id': order.product_id,
        'customer_name': order.customer_name,
        'customer_address': order.customer_address,
        'customer_phone': order.customer_phone,
        'quantity': order.quantity,
        # 'status': order.status,
        # 'created_at': order.created_at,
        # 'updated_at': order.updated_at
    } for order in orders]
    return jsonify({'orders': orders_list})

@orders_bp.route('/api/orders/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully!'})
    return jsonify({'message': 'Order not found'}), 404