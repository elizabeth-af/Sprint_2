class Movies:
    def __init__(self, movies = []):
        self.movies = movies
    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def __init__(self, movies = []):
        super().__init__(movies)

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: {self.movies}'

class Drama(Movies):
    def __init__(self, movies = []):
        super().__init__(movies)

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'

comedy = Comedy()
drama = Drama()
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))