class Actor:
    def __init__(self, first_name, last_name, birth_date, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.nationality = nationality
        self.filmography = []
        self.awards = []

    def add_film(self, film):
        self.filmography.append(film)

    def add_awards(self, award):
        self.awards.append(award)
