from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
    db = 'user_recipes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def create_recipe(cls, data):
        query = '''
        INSERT INTO recipes ( name, description, instructions, under_30_min, 
        date_made, user_id)
        VALUES ( %(name)s, %(description)s, %(instructions)s, %(under_30_min)s, 
        %(date_made)s, %(user_id)s);
        '''
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results[0])
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        all_recipes = []
        for recipe in results:
            all_recipes.append(cls(recipe))
        return all_recipes

    @classmethod
    def get_users_recipes_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        recipes = []
        print(results[0])
        for recipe in results:
            recipes.append(recipe)
        return recipes

    @classmethod
    def edit_recipe(cls, data):
        query = """ 
                UPDATE recipes 
                SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, 
                under_30_min = %(under_30_min)s, date_made = %(date_made)s,
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy_recipe(cls, data): 
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Description must be at least 3 characters.", "recipe")
            is_valid = False
        if recipe['date_made'] is None:
            flash("Date is requred.", "recipe")
            is_valid = False
        return is_valid