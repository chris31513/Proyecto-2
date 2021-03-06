from .Steve import Steve
from .DAO import DAO
from .SQLite import SQLite
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
class Control(object):
    def mine(self):
        sql = SQLite()
        sql.connect()
        minner = Steve()
        minner.get_mp3()
        minner.get_mp3_tags()
        minner.insertion()
    def consult(self):
        dao = DAO()
        return dao.consult()
    def search_path(self,song,album):
        dao = DAO()
        path = dao.search_path(song,album)[0][0]
        return path
    def search_edit(self,song,album):
        dao = DAO()
        print(song,album)
    def edit_song_name(self,new_song,old_song,album):
        dao = DAO()
        dao.edit_name(new_song,old_song,album)
    def edit_artist(self,new_artist,song,album):
        dao = DAO()
        dao.edit_artist(new_artist,song,album)
    def edit_album(self,new_album,song,album):
        dao = DAO()
        dao.edit_album(new_album,song,album)
    def search(self,list):
        dao = DAO()
        if list[0] == 'Artist:':
            return dao.search_artist(list.pop(1))
        if list[0] == 'Song:':
            return dao.search_song(list.pop(1))
        if list[0] == 'Album:':
            return dao.search_album(list.pop(1))
        
