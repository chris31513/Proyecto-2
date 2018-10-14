import os
from mutagen.id3 import ID3
from .DAO import DAO
from .Rola import Rola
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
                        if 'TPE1' in audio:
                                rola.set_artist(str(audio['TPE1']))
                        else:
                                rola.set_artist('Unknown')
                        if 'TIT2' in audio:
                                rola.set_name(str(audio['TIT2']))
                        else:
                                rola.set_name('Unknown')
                        if 'TDRC' in audio:
                                rola.set_year(str(audio['TDRC']))
                        else:
                                rola.set_year(0)
                        if 'TALB' in audio:
                                rola.set_album(str(audio['TALB']))
                        else:
                                rola.set_album('Unknown')
                        if 'TRCK' in audio:
                                s = str(audio['TRCK'])
                                try:
                                        r = int(s)
                                        rola.set_number(s)
                                except:
                                        l = s.split('/',1)
                                        rola.set_number(l[0])
                        else:
                                rola.set_number(0)
                        if 'TCON' in audio:
                                rola.set_genre(str(audio['TCON']))
                        else:
                                rola.set_genre('Unknwon')
                        self.rolas.append(rola)
        def insertion(self):
                dao = DAO()
                dao.insert(self.rolas)

