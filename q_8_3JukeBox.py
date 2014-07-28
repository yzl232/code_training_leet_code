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
    def __init__(self, song, q):
        self.song = song
        self.q = q
        
    def getNextSongToPlay(self):
        return self.q[0]
    
    def queueAddSong(self, song):
        self.q.add(s)
        
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
