from collections import queue

class Song:
    def __init__(self, songName):
        self.songName = songName
        
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class SongSelector:
    def __init__(self, s):
        self.currentSong = s
    
class Playlist:
    def __init__(self, song):
        self.song = song
        self.q = []

    def addSong(self, song):
        self.q.append(song)

    def getNextSongToPlay(self):
        if len(self.q)>0:
            return self.q.pop(0)
        return None
    
        
class JukeBox:
    def __init__(self, cdPlayer, user, cdCollection, ts):
        self.cdplayer = cdplayer
        self.user = user
        self.cdCollection = cdCollection
        self.songSelector = ts
    
    def getCurrentSong(self):
        return self.songSelector.currentSong
        
class CDPlayer:
    def __init__(self, cd, playlist):
        self.cd = cd
        self.playlist = playlist
    
    def playSong(self, song):
        pass

class CD:
    pass
