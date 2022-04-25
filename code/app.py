from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
import os


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

uri = os.getenv("DATABASE_URL")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# TODO: Externalize secret key value
app.secret_key = 'vafj'
api = Api(app)


jwt = JWT(app, authenticate, identify)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
