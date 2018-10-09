import sqlite3
class DAO(object):
    def insert(self,rolas):
        with sqlite3.connect('songs.db') as conn:
            id_type = 2
            c = conn.cursor()
            for rola in rolas:
                c.execute('''BEGIN;''')
                c.execute('''INSERT INTO performers(id_type,name) VALUES(?,?)''',(id_type,rola.get_artist(),))
                c.execute('''INSERT INTO groups(name) VALUES(?)''',(rola.get_artist(),))
                c.execute('''INSERT INTO albums(path,name,year) VALUES(?,?,?)''',(rola.get_path(),rola.get_album(),int(rola.get_year()),))
                c.execute('''INSERT INTO rolas(path,title,track,year) VALUES(?,?,?,?)''',(rola.get_path(),rola.get_name(),int(rola.get_number()),int(rola.get_year(),)))
                c.execute('''END;''')
                conn.commit()
