class Genre:
    def __init__(self, genre_name, description=None):
        self.genre_name = genre_name
        self.description = description

def find_movies_by_genre(movies, genre_name):
    result = []
    for movie in movies:
        if genre_name in [genre.genre_name for genre in movie.genres]:
            result.append(movie)
    return result