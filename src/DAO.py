import os
import sqlite3
from mutagen.id3 import ID3
class DAO(object):
    def __init__(self):
        self.rolas =[]
        pree_path = os.path.expanduser('~/.local')
        self.path = pree_path + '/'+'rolas.db'
    def insert(self,rolas):
        with sqlite3.connect(self.path) as conn:
            id_type = 2
            c = conn.cursor()
            i = 0
            for rola in rolas:
                c.execute('''SELECT path FROM rolas''')
                checker = c.fetchall()
                if (rola.get_path(),) in checker:
                    break
                else:
                    c.execute('''INSERT INTO performers(id_type,name) VALUES(?,?)''',(id_type,rola.get_artist(),))
                    c.execute('''INSERT INTO groups(name) VALUES(?)''',(rola.get_artist(),))
                    c.execute('''INSERT INTO albums(path,name,year) VALUES(?,?,?)''',(rola.get_path(),rola.get_album(),int(rola.get_year()),))
                    c.execute('''SELECT id_album FROM albums''')
                    id_album = c.fetchall()
                    c.execute('''SELECT id_performer FROM performers''')
                    id_performer = c.fetchall()
                    c.execute('''INSERT INTO rolas(id_album,id_performer,path,title,track,year) VALUES(?,?,?,?,?,?)''',(id_album.pop(i)[0],id_performer.pop(i)[0],rola.get_path(),rola.get_name(),int(rola.get_number()),int(rola.get_year(),)))
                    i += 1
                    conn.commit()
    def consult(self):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            c.execute('''SELECT track,rolas.title,albums.name,rolas.year,performers.name FROM albums,performers INNER JOIN rolas ON albums.id_album = rolas.id_album AND rolas.id_performer = performers.id_performer''')
            tabla = c.fetchall()
            return tabla
    def search_path(self,song,album):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            c.execute('''SELECT rolas.path FROM rolas,albums WHERE title = ? AND albums.name = ?''',(song,album,))
            path = c.fetchall()
            path_list = []
            true_path_list = []
            for i in path:
                if i not in path_list:
                    path_list.append(i)
            if len(path_list) > 1:
                for path in path_list:
                    audio = ID3(path[0])
                    if album == str(audio['TALB']):
                        true_path_list.append(path)
                        path_list = true_path_list
            return path_list
    def search_artist(self,artist):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            c.execute('''SELECT rolas.track,rolas.title,albums.name,rolas.year,performers.name FROM performers,albums JOIN rolas ON albums.id_album = rolas.id_album AND rolas.id_performer = performers.id_performer WHERE performers.name = ?''',(artist,))
            artist_list = c.fetchall()
            return artist_list
    def search_song(self,song):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            c.execute('''SELECT rolas.track,rolas.title,albums.name,rolas.year,performers.name FROM performers,albums JOIN rolas ON albums.id_album = rolas.id_album AND rolas.id_performer = performers.id_performer WHERE rolas.title = ?''',(song,))
            song_list = c.fetchall()
            return song_list
    def search_album(self,album):
        with sqlite3.connect(self.path) as conn:
            c = conn.cursor()
            c.execute('''SELECT rolas.track,rolas.title,albums.name,rolas.year,performers.name FROM performers,albums JOIN rolas ON albums.id_album = rolas.id_album AND rolas.id_performer = performers.id_performer WHERE albums.name = ?''',(album,))
            album_list = c.fetchall()
            return album_list
