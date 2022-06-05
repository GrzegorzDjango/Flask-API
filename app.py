from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'  # it can be other db, Postres, SQLAlchemy doesn't care
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # becase sql alchemy has a better modification tracker
app.secret_key ='grzegorz123'
api = Api(app)

# make SQLAlchemy created data.db file
@app.before_first_request
def create_tables():
    # this will create all the tables in app.config['SQLALCHEMY_DATABASE_URI'] unless the exist already
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth




api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    # sql alchemy stuff
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)