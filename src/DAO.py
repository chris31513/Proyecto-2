import sqlite3
class DAO(object):
    def __init__(self):
        self.conn = sqlite3.connect('songs.db')
    def insert_person(self,artist):
        c = self.conn.cursor()
        c.execute('''INSERT INTO performers(name) VALUES (?)''',(artist,))
        c.execute('''SELECT *
        FROM performers
        INNER JOIN types ON performers.id_type = types.id_type''')
        self.conn.commit()
    def insert_album(self,path,album,year):
        c = self.conn.cursor()
        c.execute('''INSERT INTO albums (path,name,year) VALUES (?,?,?)''', (path,album,int(year),))
        c.execute('''SELECT *
        FROM albums
        INNER JOIN rolas ON albums.id_album = rolas.id_album''')
        self.conn.commit()
    def insert_rola(self,path,title,track,year,genre):
        c = self.conn.cursor()
        c.execute('''INSERT INTO rolas(path,title,track,year,genre) VALUES (?,?,?,?,?)''',(path,title,int(track),int(year),genre,))
        c.execute('''SELECT *
        FROM rolas
        INNER JOIN performers ON rolas.id_performer = performers.id_performer''')
        self.conn.commit()
    def unplugg(self):
        self.conn.close()
