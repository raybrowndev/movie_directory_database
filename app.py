from lib.database_connection import DatabaseConnection
from lib.movie_repo import MovieRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/movie_directory.sql")

# Retrieve all artists
movie_repository = MovieRepository(connection)
movies = movie_repository.show_all()

genre_movies = movie_repository.find_by_genre("Drama/Romance")
id_movies = movie_repository.find_by_id(8)

# List them out
print("------All Movies------")
for i in movies:
    print(i)

# List drama movies
print("------Drama/Romance------")
for i in genre_movies:
    print(i)

# List drama movies
print("------ID Selection------")
for i in id_movies:
    print(i)