from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from .models import Product, Movement
from . import db

main = Blueprint('main', __name__)

@main.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@main.route('/add-product', methods=['POST'])
@login_required
def add_product():
    name = request.form['name']
    product = Product(name=name)
    db.session.add(product)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/movement', methods=['POST'])
@login_required
def movement():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])
    m_type = request.form['type']

    product = Product.query.get(product_id)

    if m_type == 'salida' and product.stock < quantity:
        flash('Stock insuficiente')
        return redirect(url_for('main.dashboard'))

    if m_type == 'entrada':
        product.stock += quantity
    else:
        product.stock -= quantity

    movement = Movement(
        type=m_type,
        quantity=quantity,
        product_id=product.id
    )

    db.session.add(movement)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
