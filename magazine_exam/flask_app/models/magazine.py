from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Magazine:
    db = 'magazine_subscriptions'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.createdat = data['createdat']
        self.updatedat = data['updatedat']
        self.user_id = data['user_id']

    def magazines(self):
        return self.title

    @staticmethod
    def validate(magazine):
        is_valid = True
        if len(magazine['title']) or len(magazine['description']) <= 0:
            is_valid=False
            flash("All fields required")
        if len(magazine['title']) < 2:
            is_valid=False
            flash("Title must be longer than 2 characters")
        if len(magazine['description']) < 10:
            is_valid=False
            flash("Description must be longer than 10 characters")
        return is_valid

    @classmethod
    def getAll(cls,data):
        query = "SELECT * FROM magazine;"
        results = connectToMySQL(cls.db).query_db(query)
        magazines = []
        for row in results:
            magazines.append(cls(row))
        return magazines

    @classmethod
    def getId(cls,data):
        query = "SELECT * FROM magazine WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO magazine (title,description,user_id) VALUES (%(title)s,%(description)s,%(user_id)s);'
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE magazine SET title=%(title)s, description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM magazine WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def allMagazines(cls):
        query = 'SELECT * FROM magazine JOIN user on magazine.user_id = user.id;'
        results = connectToMySQL(cls.db).query_db(query)
        print('All magazines: ', results)
        return results
