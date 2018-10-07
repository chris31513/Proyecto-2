class Rola(object):
    def __init__(self):
        self.artist = ""
        self.name = ""
        self.year = ""
        self.album = ""
        self.number = ""
        self.path = ""
        self.genre = ""
    def set_path(self,path):
        self.path = path
    def set_artist(self,artist):
        self.artist = artist
    def set_name(self,name):
        self.name = name
    def set_year(self,year):
        self.year = year
    def set_album(self,album):
        self.album = album
    def set_number(self,number):
        self.number = number
    def set_genre(self,genre):
        self.genre = genre
    def get_artist(self):
        return self.artist
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_number(self):
        return self.number
    def get_album(self):
        return self.album
    def get_path(self):
        return self.path
