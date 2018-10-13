import sys
sys.path.append("..")
import gi
from src.Control import Control
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import warnings
warnings.filterwarnings("ignore")

class MyWindow(Gtk.Window):

    def __init__(self):
        control = Control()
        control.mine()
        rolas_list = control.consult()
        Gtk.Window.__init__(self, title="Rolas")
        self.set_border_width(10)
        self.set_default_size(500,500)
        self.albums = []
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)
        for i in control.consult():
            if i[2] not in self.albums:
                self.albums.append(i[2])
        self.albums.append("None")
        self.rolas_liststore = Gtk.ListStore(int, str, str,int)
        self.rolas_liststore.set_sort_column_id(0, Gtk.SortType.ASCENDING)
        for rolas_ref in rolas_list:
            self.rolas_liststore.append(list(rolas_ref))
        self.current_filter_album = None
        self.album_filter = self.rolas_liststore.filter_new()
        self.album_filter.set_visible_func(self.album_filter_func)
        self.buttons = list()
        for album in self.albums:
            button = Gtk.Button(album)
            self.buttons.append(button)
            button.connect("clicked", self.on_selection_button_clicked)
        self.treeview = Gtk.TreeView.new_with_model(self.album_filter)
        for i, column_title in enumerate(["Numero", "Rola", "Album","Año"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.scrollable_treelist.add(self.treeview)
        self.show_all()
    def album_filter_func(self, model, iter, data):
        if self.current_filter_album is None or self.current_filter_album == "None":
            return True
        else:
            return model[iter][2] == self.current_filter_album

    def on_selection_button_clicked(self, widget):
        self.current_filter_album = widget.get_label()
        print("%s album selected!" % self.current_filter_album)
        self.album_filter.refilter()    
window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
