from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
NUMBOXES_REGEX = re.compile(r'^[1-9]\d*$')
class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_user( order ):
        is_valid = True
        if len(order['customer_name']) < 0 or len(order['customer_name']) < 2:
            flash("Name must be at least 2 characters!")
            is_valid = False
        if  len(order['cookie_type']) < 0 or len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters!")
            is_valid = False
        if not NUMBOXES_REGEX.match(order['num_boxes']):
            flash('Positive integers only!')
            is_valid = False
        for customer_name in Order.get_all():
            if order['customer_name'] == customer_name.customer_name and order['cookie_type'] == customer_name.cookie_type: 
                flash("This data already  exists!")
                is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = "INSERT INTO orders(customer_name,cookie_type, num_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_boxes)s);"
        return  connectToMySQL('cookie_orders').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders

    @classmethod
    def update(cls, form_data):
        query = "UPDATE orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, num_boxes=%(num_boxes)s WHERE id = %(id)s"
        return  connectToMySQL('cookie_orders').query_db(query, form_data)

    @classmethod
    def get_one(cls, data):
        query = " SELECT * FROM orders WHERE  id = %(id)s;"
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(results[0])