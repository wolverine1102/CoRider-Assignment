from flask_pymongo import PyMongo
from flask import current_app as app

validator = {"$jsonSchema": {
    "bsonType": "object",
    "required": [ "id", "name", "email", "password" ]
}}

db = PyMongo(app).db
if "User" not in db.list_collection_names():
    db.create_collection("User")
db.command("collMod", "User", validator=validator)    
db.User.create_index([
    ("id", 1)
], unique=True)
