from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = 'magazine_subscriptions'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.createdat = data['createdat']
        self.updatedat = data['updatedat']

    def fullName(self):
            return f'{self.first_name} {self.last_name}'

    @staticmethod
    def validate(user):
            is_valid = True
            query = "SELECT * FROM user WHERE email = %(email)s;"
            results = connectToMySQL(User.db).query_db(query,user)
            if len(results) >= 1:
                flash("Email already taken.")
                is_valid=False
            if not EMAIL_REGEX.match(user['email']):
                is_valid=False
                flash("Invalid Email")
            if len(user['first_name']) < 3:
                is_valid= False
                flash("First name must be at least 3 characters")
            if len(user['last_name']) < 3:
                is_valid= False
                flash("Last name must be at least 3 characters")
            if len(user['password']) < 8:
                is_valid= False
                flash("Password must be at least 8 characters")
            if user['password'] != user['confirm']:
                flash("Passwords don't match")
            return is_valid

    @classmethod
    def getAll(cls):
            query = "SELECT * FROM user;"
            results = connectToMySQL(cls.db).query_db(query)
            users = []
            for row in results:
                users.append( cls(row))
            return users

    @classmethod
    def getId(cls,data):
            query = "SELECT * FROM user WHERE id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return cls(results[0])

    @classmethod
    def getEmail(cls,data):
            query = "SELECT * FROM user WHERE email = %(email)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return cls(results[0])

    @classmethod
    def save(cls,data):
        query = 'INSERT INTO user (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'
        return connectToMySQL(cls.db).query_db(query,data)


