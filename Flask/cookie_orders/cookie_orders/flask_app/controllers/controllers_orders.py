from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models.models_order import Order
from flask_app.config.mysqlconnection import connectToMySQL


@app.route('/')
def index():
    orders = Order.get_all()
    return render_template('index.html', orders=orders)

@app.route('/new_order')
def new_user():
    return render_template('new_order.html')


@app.route('/create_order', methods=['POST'])
def create_user():
    if not Order.validate_user(request.form):
        return redirect('/new_order')
    Order.create(request.form)
    return redirect('/')

@app.route('/update/<int:order_id>', methods=['POST'])
def update_order(order_id):
    if not Order.validate_user(request.form):
        return  redirect(f'/edit/{order_id}')
    data = {
        'id' : order_id,
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes': request.form['num_boxes']
    }
    Order.update(data)
    return redirect('/')

@app.route('/edit/<int:order_id>')
def edit_order(order_id):
    data = {
        'id' : order_id
    }
    return render_template('edit_order.html', order = Order.get_one(data))