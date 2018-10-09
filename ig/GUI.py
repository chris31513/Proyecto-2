import sys
sys.path.append("..")
from src.Steve import Steve
import src.SQLite as s
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Rolas")
        s
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        mine = Steve()
        mine.get_mp3()
        mine.get_mp3_tags()
        mine.insertion()
        for rola in mine.rolas:
            print(rola.get_name())
        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
