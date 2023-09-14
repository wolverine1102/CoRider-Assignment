from flask_pymongo import PyMongo
from flask import current_app as app

validator = {"$jsonSchema": {
    "bsonType": "object",
    "required": [ "id", "name", "email", "password" ]
}}

db = PyMongo(app).db
db.command("collMod", "User", validator=validator)    # Assuming "User" collection exits in the database.
db.User.create_index([
    ("id", 1)
], unique=True)
