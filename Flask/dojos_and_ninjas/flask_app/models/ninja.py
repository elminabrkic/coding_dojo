
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.dojos_id = data['dojos_id']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM ninjas"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_ninjas=[]
        for ninja in results:
            all_ninjas.append(cls(ninja))
        return all_ninjas

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojos_id) VALUES (%(first_name)s , %(last_name)s , %(age)s, %(dojos_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        


        