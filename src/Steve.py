import os
from mutagen.id3 import ID3
from DAO import DAO
from Rola import Rola
class Steve(object):
        def __init__(self):
                self.filepath = []
                self.rolas = []
        def get_mp3(self):
                newpath = os.path.expanduser('~/Music')
                for root, dirs, files in os.walk(newpath):
                        for file in files:
                                self.filepath.extend([os.path.join(root,file)])
        def get_mp3_tags(self):
                for i in self.filepath:
                        audio = ID3(i)
                        rola = Rola()
                        rola.set_path(i)
                        rola.set_artist(str(audio['TPE1']))
                        rola.set_name(str(audio['TIT2']))
                        rola.set_year(str(audio['TDRC']))
                        rola.set_album(str(audio['TALB']))
                        rola.set_number(str(audio['TRCK']))
                        self.set_genre(str(audio['TCON']))
                        self.rolas.append(rola)
        def insertion(self):
                dao = DAO()
                for i in self.rolas:
                        dao.insert_album(i.get_path(),i.get_album(),i.get_year())
                        dao.insert_person(i.get_artist())
                        dao.insert_rola(i.get_path(),i.get_name(),i.get_number(),i.get_year(), i.get_genre())
                dao.unplugg()
