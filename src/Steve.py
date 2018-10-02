import os
import eyed3
eyed3.log.setLevel("ERROR")
class Steve(object):
        def __init__(self):
                self.filepath = []
                self.carp = []
                self.artist = []
                self.albums = []
                self.songs = []
        def get_mp3(self):
                newpath = os.path.expanduser('~/Music')
                for root, dirs, files in os.walk(newpath):
                        for file in files:
                                self.filepath.extend([os.path.join(root,file)])
        def get_mp3_tags(self):
                for i in self.filepath:
                        audio = eyed3.load(i)
                        self.artist.append(audio.tag.artist)
                        self.albums.append(audio.tag.album)
                        self.songs.append(audio.tag.title)

                        



