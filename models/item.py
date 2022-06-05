import sqlite3
from db import db

class ItemModel(db.Model):
    # sql alchemy stuff, like for users
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # to find store in db
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()
        # was simplified by SQLAlchemy

        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()

        # query = "select * from items where name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # conn.close()

        # if row:
        #     return cls(*row)  # unpacking cls(row[0], row[1])
        #     # return {'item': {'name': row[0], 'price': row[1]}}


    # def insert(self):   # it's inserting itself so no class method
    # insert and updae can be replace by save_to_db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # SQLAlchemy update code below
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # query = "insert into items values (?,?)"
        # cursor.execute(query, (self.name, self.price))
        # conn.commit()
        # conn.close()

    # def update(self):
    #     conn = sqlite3.connect('data.db')
    #     cursor = conn.cursor()
    #     query = "update items set price=? where name=?"
    #     cursor.execute(query, (self.name, self.price))
    #     conn.commit()
    #     conn.close()
    #     return {'message': 'item deleted'}
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()