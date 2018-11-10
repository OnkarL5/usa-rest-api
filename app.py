from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister, User

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'omai-key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/api/register')
api.add_resource(User, '/api/user/<string:username>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run()
