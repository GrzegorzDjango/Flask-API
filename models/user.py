import sqlite3
from db import db
class UserModel(db.Model):
    #sql alechemy features
    __tablename__ = 'users'
    # alchemy columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # don't need to include id as it's primary key
    def __init__(self, username, password):
        # names here must match sql alechmy columns
        self.username = username
        self.password = password
    
    def saved_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        # conn = sqlite3. connect('data.db')
        # cursor = conn.cursor()

        # query = "select * from users where username=?"
        # # all params must be in the form of a tuple
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()

        # if row:
        #     user = cls(*row)   #cls(row[0], row[1], row[2])
        # else:
        #     user = None
        
        # conn.close()
        # return  user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # conn = sqlite3. connect('data.db')
        # cursor = conn.cursor()

        # query = "select * from users where id=?"
        # # all params must be in the form of a tuple
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()

        # if row:
        #     user = cls(*row)   #cls(row[0], row[1], row[2])
        # else:
        #     user = None
        
        # conn.close()
        # return  user