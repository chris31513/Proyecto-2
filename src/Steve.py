import os
import eyed3
eyed3.log.setLevel("ERROR")
class Steve(object):
        def __init__(self):
                self.artist = []
                self.albums = []
                self.songs = []
        def get_mp3(self):
                newpath = os.path.expanduser('~/Music')
                for root, dirs, files in os.walk(newpath):
                        return files
        def get_mp3_tags(self):
                for i in self.get_mp3():
                        audio = eyed3.load(os.path.expanduser('~/Music')+'/'+i)
                        self.artist.append(audio.tag.artist)
                        self.albums.append(audio.tag.album)
                        self.songs.append(audio.tag.title)


