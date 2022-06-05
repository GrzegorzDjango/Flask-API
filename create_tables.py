import sqlite3

# with SQLAlchemy we don't really need this script
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_table = "create table if not exists users (id integer primary key, username text, password text)"
cursor.execute(create_table)

create_table = "create table if not exists items (id integer primary key, name text, price real)"
cursor.execute(create_table)


conn.commit()
conn.close()
