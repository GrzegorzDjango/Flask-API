import sqlite3
from db import db

# new SQLAlchemy model from scratch
class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # get all the items in the store
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json()  for item in self.items.all()]} # .all() because we used lazy='dynamic' which is a query builder, until we look into json method we don't look into items table

    @classmethod
    def find_by_name(cls, name):
        return StoreModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()