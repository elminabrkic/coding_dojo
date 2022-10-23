from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user( user ):
        is_valid = True
        if len(user['first_name']) < 1:
            flash("Invalid first name!")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Invalid last name!")
            is_valid = False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        for email in User.get_all():
            if user['email'] == email.email:
                flash("This email is taken!")
                is_valid = False
        return is_valid
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users(first_name,last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return  connectToMySQL('user_schema').query_db(query,data)

    @classmethod
    def update(cls, form_data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email=%(email)s WHERE id = %(id)s"
        return  connectToMySQL('user_schema').query_db(query, form_data)



    @classmethod
    def get_one(cls, data):
        query = " SELECT * FROM users WHERE  id = %(id)s;"
        results = connectToMySQL('user_schema').query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return  connectToMySQL('user_schema').query_db(query, data)



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    

