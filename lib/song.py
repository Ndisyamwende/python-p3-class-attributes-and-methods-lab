class Song:
    count = 0
    artists = set()
    genres = set()
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1 #the ++shows increament when new song is created
        Song.artists.add(artist)
        Song.genres.add(genre)

        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count
    
    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
