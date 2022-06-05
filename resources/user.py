#user sqlite3

import sqlite3
from unittest import result
from flask import request
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="cannot be blank")
    parser.add_argument('password', type=str, required=True, help="cannot be blank")
        
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "user with that username already exists"}, 400

        user = UserModel(**data)  # equiv of UserModel(data['username'], data['password'])
        user.saved_to_db()
        # SQLAlchemy simplifies below

        # conn  = sqlite3.connect('data.db')
        # cursor = conn.cursor()
     
        # query = "insert into users values (NULL, ?, ?)"
        # cursor.execute(query, (data['username'], data['password']))
        
        # conn.commit()
        
        # conn.close()
        
        return {"message", "user created successfully."}, 201