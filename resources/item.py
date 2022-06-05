from turtle import update
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help='cannot be blank')
    parser.add_argument('store_id',type=int,required=True,help='cannot be blank')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()  # method we defined
        return {'message': 'item not found'}, 404

        # item = next(filter(lambda x: x['name']==name, items), None)

        # return {'item': item}, 200 if item else 404



    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)}, 400  # bad request 400
        # if next(filter(lambda x: x['name']==name, items), None) is not None:
        #     return {'message': "An item with name '{}' already exist".format(name)}, 400  # bad request 400

        request_data = Item.parser.parse_args()
        price = request_data['price']
        store_id = request_data['store_id']
        item = ItemModel(name, price, store_id)  # no longer dict {'name': name, 'price': price}
        try:
            # self.insert(item)
            # item.insert()  # method we defined
            item.save_to_db()
        except:
            return {"message": "error occured while inserting"}, 500 # internal server error
        # items.append(item)
        
        return item, 201  # to tell postman, 201 = successfully created object

    def delete(self, name):
        # SQLAlchemy replaces code below
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # query = "delete from items where name=?"
        # cursor.execute(query, (name,))
        # conn.commit()
        # conn.close()
        # return {'message': 'item deleted'}
        

    def put(self, name):
        # request_data = request.get_json()
        request_data = Item.parser.parse_args()
        price = request_data['price']
        store_id = request_data['store_id']
        # item = next(filter(lambda x: x['name']==name, items), None)

        item = ItemModel.find_by_name(name)
        
        # updated_item = ItemModel(name, price)  # {'name': name, 'price': price}
        if item is None:
            item = ItemModel(name, price, store_id) # equiv ItemModel(name, **data)
        else:
            item.price = price
            item.store_id = store_id
        #     try:
               
        #         # ItemModel.insert(updated_item)
        #         updated_item.insert()
        #     except:
        #         return {'message': 'error inserting the item'}, 500
        # else:
        #     try:
        #         # ItemModel.update(updated_item)
        #         updated_item.update()
        #     except:
        #         return {'message': 'error updating the item'}, 500
        item.save_to_db()
        return item.json() 


class ItemList(Resource):
    def get(self):
        # SQLAlchemy
        # return {'items': [item.json() for item in ItemModel.query.all()]}
        return {'items': list(map(lambda x: x.json(),ItemModel.query.all()))}
        # return {'items': items}
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # query = "select * from items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0],'price':row[1]})
        # conn.commit()
        # conn.close()

        # return {'items': items}