from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/DB"
app.app_context().push()

from application.UserAPI import *

api.add_resource(UserAPI, '/users/', '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True, 
            port=5000)
