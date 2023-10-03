from lib.movie import Movie

class MovieRepository:
    def __init__(self, connection):
        self._connection = connection 

    def show_all(self):
        movies = self._connection.execute('SELECT * FROM movie')
        movie_list = []
        for i in movies:
            items = Movie(i['id'], i['title'], i['genre'], i['release_year'])
            movie_list.append(items)
        return movie_list 

    def find_by_genre(self, search_genre):
        movies = self._connection.execute('SELECT * FROM movie WHERE genre = %s', [search_genre])
        movie_list = []
        for i in movies:
            items = Movie(i['id'], i['title'], i['genre'], i['release_year'])
            movie_list.append(items)
        return movie_list 

    def find_by_id(self, search_id):
        movies = self._connection.execute('SELECT * FROM movie WHERE id = %s', [search_id])
        movie_list = []
        for i in movies:
            items = Movie(i['id'], i['title'], i['genre'], i['release_year'])
            movie_list.append(items)
        return movie_list 
