class Movie:
    def __init__(self, rating, movie_name, movie_description, genres, release_date, actors):
        self.rating = rating
        self.movie_name = movie_name
        self.movie_description  = movie_description
        self.genres = genres
        self.release_date = release_date
        self.actors = actors

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        self.actors.remove(actor)

    def add_genre(self, genre):
        self.genres.append(genre)

    def remove_genre(self, genre):
        self.genres.remove(genre)