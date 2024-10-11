class Movie:
    def __init__(self, title, year, genre, id=None):
        self.title = title
        self.year = year
        self.genre = genre
        self.id = id

    def save(self, db):
        if self.db:
            db.update('movies', {'title': self.title, 'year': self.year, 'genre': self.genre}, f"id={self.id}")
        else:
            db.insert('movies', {'title': self.title, 'year': self.year, 'genre': self.genre})
            result = db.fetchall(
                f"SELECT id FROM movies WHERE title='{self.title}' AND year={self.year} AND genre='{self.genre}'")
            self.id = result[0][0]

    def delete(self, db):
        db.delete('movies', f"id={self.id}")

    @classmethod
    def get_by_id(cls, db, movie_id):
        query = f"SELECT * FROM movies WHERE id={movie_id}"
        result = db.fetchall(query)
        if result:
            return cls(*result[0][1:])
        return None

    @classmethod
    def search(cls, db, title=None, year=None, genre=None):
        query = "SELECT * FROM movies"
        conditions = []
        if title:
            conditions.append(f"title LIKE '%{title}%'")
        if year:
            conditions.append(f"year={year}")
        if genre:
            conditions.append(f"genre='{genre}'")
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        results = db.fetchall(query)
        return [cls(*result[1:]) for result in results]

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.genre}"