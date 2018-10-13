import sys
sys.path.append('..')
import threading
from src.Control import Control
import vlc
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import warnings
warnings.filterwarnings('ignore')


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title = 'Rolas')
        album_for_menu = []
        self.songs = []
        self.set_default_size(500,500)
        layout = Gtk.VBox()
        main_menu = Gtk.MenuBar()
        menu = Gtk.Menu()
        menu_player = Gtk.Menu()
        album_dropdown = Gtk.MenuItem("Albums")
        album_dropdown.set_submenu(menu)
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_vexpand(True)
        scroll_window.add(layout)
        self.add(scroll_window)
        self.control = Control()
        self.control.mine()
        rolas = self.control.consult()
        rolas_list_store = Gtk.ListStore(int,str,str,int)
        for rola in rolas:
            rolas_list_store.append(list(rola))
            if rola[2] not in album_for_menu:
                album_for_menu.append(rola[2])
        album_for_menu.append("None")
        for album in album_for_menu:
            album = Gtk.MenuItem(album)
            album.set_hexpand(False)
            album.connect("activate",self.on_selection_button_clicked)
            menu.append(album)
        self.current_filter_album = None
        self.album_filter = rolas_list_store.filter_new()
        self.album_filter.set_visible_func(self.album_filter_func)
        main_menu.append(album_dropdown)
        pre_rolas_tree = Gtk.TreeModelSort(self.album_filter)
        rolas_tree = Gtk.TreeView(pre_rolas_tree)
        for i,title in enumerate(["Track", "Name", "Album","Year"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(title,renderer,text = i)
            column.set_sort_column_id(i)
            column.set_clickable(True)
            rolas_tree.append_column(column)
        song_selected = rolas_tree.get_selection()
        song_selected.connect("changed",self.play_song)
        player_dropdown = Gtk.MenuItem("Player")
        pause = Gtk.MenuItem("Pause")
        stop = Gtk.MenuItem("Stop")
        player_dropdown.set_submenu(menu_player)
        pause.connect("activate",self.pause)
        stop.connect("activate",self.stop)
        menu_player.append(pause)
        menu_player.append(stop)
        main_menu.append(player_dropdown)
        layout.pack_start(main_menu,False,False,0)
        layout.pack_start(rolas_tree,True,True,0)
    def stop(self,widget):
        self.songs[0].stop()
    def pause(self,widget):
        self.songs[0].pause()
    def album_filter_func(self, model, iter, data):
        if self.current_filter_album is None or self.current_filter_album == "None":
            return True
        else:
            return model[iter][2] == self.current_filter_album
    def on_selection_button_clicked(self, widget):
        self.current_filter_album = widget.get_label()
        print("%s album selected!" % self.current_filter_album)
        self.album_filter.refilter()
    def play_song(self,selection):
        try:
            model,row = selection.get_selected()
            song = vlc.MediaPlayer(self.control.search_path(model[row][1]))
            self.songs.append(song)
            self.songs[0].play()
            self.songs[0].stop()
            if len(self.songs) > 1:
                self.songs[0].stop()
                self.songs.pop(0)
                self.songs[0].play()
        except:
            pass
window = MyWindow()
window.connect('destroy',Gtk.main_quit)
window.show_all()
Gtk.main()
