class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.watched_movies = []
        self.reviews = []
        self.favorite_genre = []

    def add_watched_movies(self, movie):
        self.watched_movies.append(movie)

    def add_review(self, review):
        self.reviews.append(review)

    def add_favorite_genre(self, genre):
        self.favorite_genre.append(genre)
