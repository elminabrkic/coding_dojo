from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']
        self.ninjas = []

    @classmethod
    def create(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojos=[]
        for dojo in results:
            all_dojos.append(cls(dojo))
        return all_dojos


    @classmethod
    def get_name(cls, id):
        query = f"SELECT name FROM dojos WHERE id={id}"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        one_dojo = cls(results[0])
        for one_ninja in results:
            if  one_ninja['ninjas.id'] == None:
                break
            data = {
                'id': one_ninja['ninjas.id'],
                'first_name': one_ninja['first_name'],
                'last_name': one_ninja['last_name'],
                'age': one_ninja['age'],
                'created_at': one_ninja['created_at'],
            }
            ninja_obj = ninja.Ninja(data)
            print( ninja_obj)
            one_dojo.ninjas.append(ninja_obj)
        return one_dojo