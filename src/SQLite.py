import sqlite3
conn = sqlite3.connect('songs.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS types (
id_type
INTEGER PRIMARY KEY ,
description
TEXT
);''')
cur.execute('''INSERT INTO types VALUES (0 , 'Person');''')
cur.execute('''INSERT INTO types VALUES (1 , 'Group');''')
cur.execute('''INSERT INTO types VALUES (2 , 'Unkwon');''')

cur.execute('''CREATE TABLE performers (
id_performer INTEGER PRIMARY KEY ,
id_type
INTEGER ,
name
TEXT ,
FOREIGN KEY
( id_type ) REFERENCES types ( id_type )
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS persons (
id_person
INTEGER PRIMARY KEY ,
stage_name
TEXT ,
real_name
TEXT ,
birth_date
TEXT ,
death_date
TEXT
);''')
cur.execute('''CREATE TABLE IF NOT EXISTS groups (
id_group
INTEGER PRIMARY KEY ,
name
TEXT ,
start_date
TEXT ,
end_date
TEXT
);''')
cur.execute('''CREATE TABLE IF NOT EXISTS albums (
id_album
INTEGER PRIMARY KEY ,
path
TEXT ,
name
TEXT ,
year
INTEGER
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS rolas (
id_rola
INTEGER PRIMARY KEY ,
id_performer INTEGER ,
id_album
INTEGER ,
path
TEXT ,
title
TEXT ,track
INTEGER ,
year
INTEGER ,
genre
TEXT ,
FOREIGN KEY
( id_performer )
REFERENCES performers ( id_performer ),
FOREIGN KEY
( id_album )
REFERENCES albums ( id_album )
);''')
cur.execute('''CREATE TABLE IF NOT EXISTS in_group (
id_person
INTEGER ,
id_group
INTEGER ,
PRIMARY KEY
( id_person , id_group ),
FOREIGN KEY
( id_person ) REFERENCES persons ( id_person ),
FOREIGN KEY
( id_group ) REFERENCES groups ( id_group )
);''')

conn.commit()
conn.close()
