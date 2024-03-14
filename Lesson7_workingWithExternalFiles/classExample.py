#create a class to represent a song on Spotify
class Song:
    #constructor
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
    #method to print the song details
    def printSong(self):
        print("Title: ", self.title)
        print("Artist: ", self.artist)
        print("Album: ", self.album)
        print("Length: ", self.length)

#test the Song class
song1 = Song("Cruel Summer", "Taylor Swift", "1989", "3:16")

song1.printSong()