if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from src.Control import Control
    else:
        from ..src.Control import Control
import vlc
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import warnings
warnings.filterwarnings('ignore')
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title = 'Rolitas')
        self.set_icon_from_file('icon/compact-disc.svg')
        self.album_for_menu = []
        self.songs = []
        self.song_p = []
        self.album_p = []
        self.set_default_size(1000,500)
        self.song_s = []
        self.album_s = []
        self.num_s = []
        self.year_s = []
        self.artist_s = []
        layout = Gtk.VBox()
        self.searchentry = Gtk.SearchEntry()
        self.searchentry.connect("activate",self.search)
        layout.pack_start(self.searchentry,False,False,0)
        main_menu = Gtk.MenuBar()
        edit_menu = Gtk.Menu()
        menu_player = Gtk.Menu()
        refresh_menu = Gtk.Menu()
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_vexpand(True)
        scroll_window.add(layout)
        self.add(scroll_window)
        self.control = Control()
        self.rolas = []
        self.rolas_list_store = Gtk.ListStore(int,str,str,int,str)
        self.rolas_tree = Gtk.TreeView(self.rolas_list_store)
        for i,title in enumerate(["Track", "Name", "Album","Year","Artist"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title,renderer,text = i)
            column.set_sort_column_id(i)
            column.set_clickable(True)
            self.rolas_tree.append_column(column)
        song_selected = self.rolas_tree.get_selection()
        song_selected.connect("changed",self.get_selection)
        player_dropdown = Gtk.MenuItem("Player")
        edit_dropdown = Gtk.MenuItem("Edit Tags")
        pause = Gtk.MenuItem("Pause")
        play = Gtk.MenuItem("Play")
        play.connect("activate",lambda x: self.play_song(play))
        edit = Gtk.MenuItem("Edit")
        edit.connect("activate",self.edit_tags)
        stop = Gtk.MenuItem("Stop")
        refresh = Gtk.MenuItem("Refresh")
        miner = Gtk.MenuItem("Mine")
        search_r = Gtk.MenuItem("Search")
        search_r.connect("activate",self.refresh_search)
        miner.connect("activate", self.minar)
        refresh.set_submenu(refresh_menu)
        refresh_menu.append(miner)
        refresh_menu.append(search_r)
        main_menu.append(refresh)
        player_dropdown.set_submenu(menu_player)
        edit_dropdown.set_submenu(edit_menu)
        pause.connect("activate",self.pause)
        stop.connect("activate",self.stop)
        menu_player.append(play)
        menu_player.append(pause)
        menu_player.append(stop)
        edit_menu.append(edit)
        main_menu.append(player_dropdown)
        main_menu.append(edit_dropdown)
        layout.pack_start(main_menu,False,False,0)
        layout.pack_start(self.rolas_tree,True,True,0)
    def get_selection(self,selection):
        try:
            model,row = selection.get_selected()
            self.num_s.append(model[row][0])
            self.song_s.append(model[row][1])
            self.song_p.append(model[row][1])
            self.album_s.append(model[row][2])
            self.album_p.append(model[row][2])
            self.year_s.append(model[row][3])
            self.artist_s.append(model[row][4])
        except:
            pass
    def stop(self,widget):
        try:
            self.songs[0].stop()
            self.songs.pop(0)
            self.song_p.pop(0)
            self.album_p.pop(0)
        except:
            pass
    def pause(self,widget):
        self.songs[0].pause()
    def edit_tags(self,widget):
        self.new_window = Gtk.Window(title = "Edit")
        self.new_window.connect("delete-event",Gtk.main_quit)
        box = Gtk.VBox()
        entry = Gtk.Entry()
        entry.connect("activate",self.maneja)
        box.pack_start(entry,False,False,0)
        self.new_window.add(box)
        self.new_window.show_all()
        Gtk.main()
    def maneja(self,entry):
        l = entry.get_text().split(maxsplit = 1)
        entry.set_text("")
        if l[0] == "Song:":
            while len(self.song_s) != 1:
                self.song_s.pop(0)
            while len(self.album_s) != 1:
                self.album_s.pop(0)
            self.control.edit_song_name(l[1],self.song_s.pop(0),self.album_s.pop(0))
            self.minar(None)
            self.new_window.destroy()
            self.stop(None)
        if l[0] == "Artist:":
            while len(self.song_s) != 1:
                self.song_s.pop(0)
            while len(self.album_s) != 1:
                self.album_s.pop(0)
            self.control.edit_artist(l[1],self.song_s.pop(0),self.album_s.pop(0))
            self.minar(None)
            self.new_window.destroy()
            self.stop(None)
        if l[0] == "Album:":
            while len(self.song_s) != 1:
                self.song_s.pop(0)
            while len(self.album_s) != 1:
                self.album_s.pop(0)
            self.control.edit_album(l[1],self.song_s.pop(0),self.album_s.pop(0))
            self.minar(None)
            self.new_window.destroy()
            self.stop(None)
    def play_song(self,widget):
        try:
            while len(self.song_p) != 1:
                self.song_p.pop(0)
            while len(self.album_p) != 1:
                self.album_p.pop(0)
            song = vlc.MediaPlayer(self.control.search_path(self.song_p.pop(0),self.album_p.pop(0)))
            self.songs.append(song)
            self.songs[0].play()
            if len(self.songs) > 1:
                self.songs[0].stop()
                self.songs.pop(0)
                self.songs[0].play()
        except:
            pass
    def refresh_search(self,widget):
        self.rolas_tree.set_model(self.rolas_list_store)
    def minar(self,widget):
        self.rolas_list_store.clear()
        self.control.mine()
        self.rolas = self.control.consult()
        for rola in self.rolas:
            self.rolas_list_store.append(list(rola))
        self.rolas_tree.set_model(self.rolas_list_store)
    def search(self,entry):
        try:
            search = entry.get_text().split(maxsplit=1)
            new_list_store = Gtk.ListStore(int,str,str,int,str)
            for i in self.control.search(search):
                new_list_store.append(list(i))
            self.rolas_tree.set_model(new_list_store)
            entry.set_text('')
        except:
            self.rolas_tree.set_model(self.rolas_list_store)
window = MyWindow()
window.connect('destroy',Gtk.main_quit)
window.show_all()
Gtk.main()
