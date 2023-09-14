from flask_restful import Resource, fields, marshal_with, reqparse, marshal
from flask import current_app as app
from pymongo import ReturnDocument
from .database import db
from .validation import *


# Request Parser JSON
user_request_parse = reqparse.RequestParser()
user_request_parse.add_argument('id', required=True)
user_request_parse.add_argument('name', required=True)
user_request_parse.add_argument('email', required=True)
user_request_parse.add_argument('password', required=True)

# API Response Field
user_response_fields = {
    "id": fields.String,
    "name": fields.String,
    "email": fields.String,
    "password": fields.String
}


@app.route('/users/')
def users():
    users = db.User.find({})
    users_list = []
    for user in users:
        users_list.append(marshal(user, user_response_fields))

    if (users_list == []):
        raise NotFoundError(status_code=404, error_message="No users found")
    else:
        return jsonify(users_list)
    
    
class UserAPI(Resource):

    @marshal_with(user_response_fields)
    def get(self, id):
        user = db.User.find_one({"id" : id})
        if user:
            return user, 200
        else:
            raise NotFoundError(status_code=404, error_message="User %s not found" %(id))
        

    def delete(self, id):
        user = db.User.find_one_and_delete({"id" : id})
        if user:
            return '', 200
        else:
            raise NotFoundError(status_code=404, error_message="User %s not found" %(id))
        

    @marshal_with(user_response_fields)
    def put(self, id):
        args = user_request_parse.parse_args()
        name = args.get('name')
        email = args.get('email')
        password = args.get('password')

        if (name == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Name is a required parameter and cannot be empty')
        if (email == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Email is a required parameter and cannot be empty')
        if (password == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Password is a required parameter and cannot be empty')

        user = db.User.find_one_and_update(
            {"id" : id}, 
            {"$set" : {
                "name" : name,
                "email" : email,
                "password" : password
            }},
            return_document=ReturnDocument.AFTER)
        if user:
            return user, 200
        else:
            raise NotFoundError(status_code=404, error_message="User %s not found" %(id))

    
    @marshal_with(user_response_fields)
    def post(self):
        args = user_request_parse.parse_args()
        id = args.get('id')
        name = args.get('name')
        email = args.get('email')
        password = args.get('password')

        if (id == ''):
            raise BusinessValidationError(
                status_code=400, error_message='ID is a required parameter and cannot be empty')
        if (name == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Name is a required parameter and cannot be empty')
        if (email == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Email is a required parameter and cannot be empty')
        if (password == ''):
            raise BusinessValidationError(
                status_code=400, error_message='Password is a required parameter and cannot be empty')
        
        try:
            db.User.insert_one({
                "id" : id,
                "name" : name,
                "email" : email,
                "password" : password
            })
            return db.User.find_one({"id" : id}), 200
        except:
            raise AlreadyExist(status_code=409, error_message='User ID already exists')
