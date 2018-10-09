import sqlite3
class DAO(object):
    def insert(self,rolas):
        with sqlite3.connect('songs.db') as conn:
            id_type = 2
            c = conn.cursor()
            i = 0
            for rola in rolas:
                c.execute('''SELECT title FROM rolas''')
                checker = c.fetchall()
                if (rola.get_name(),) in checker:
                    break
                c.execute('''BEGIN;''')
                c.execute('''INSERT INTO performers(id_type,name) VALUES(?,?)''',(id_type,rola.get_artist(),))
                c.execute('''INSERT INTO groups(name) VALUES(?)''',(rola.get_artist(),))
                c.execute('''INSERT INTO albums(path,name,year) VALUES(?,?,?)''',(rola.get_path(),rola.get_album(),int(rola.get_year()),))
                c.execute('''SELECT id_album FROM albums''')
                id_album = c.fetchall()
                c.execute('''SELECT id_performer FROM performers''')
                id_performer = c.fetchall()
                c.execute('''INSERT INTO rolas(id_album,id_performer,path,title,track,year) VALUES(?,?,?,?,?,?)''',(id_album.pop(i)[0],id_performer.pop(i)[0],rola.get_path(),rola.get_name(),int(rola.get_number()),int(rola.get_year(),)))
                i += 1
                c.execute('''END;''')
                conn.commit()
