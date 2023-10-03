# Single Table Design Recipe Template - Movie Directory



## 1. Extract nouns from the user stories or specification

```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.
```

```
Nouns:

movie, genre, release year
```

## 2. Infer the Table Name and Columns


| Record                | Properties                  |
| --------------------- | --------------------------- |
| Movies                 | title, genre ,release year |

Name of the table (always plural): `albums`

Column names: `title`, `genre`, `release_year`

## 3. Decide the column types

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
genre: text
release_year: int
```

## 4. Write the SQL

```sql
-- file: movie_directory.sql

CREATE SEQUENCE IF NOT EXISTS movie_id_seq;

CREATE TABLE movie (
    id SERIAL PRIMARY KEY,
    title text,
    genre text,
    release_year int
);

INSERT INTO movie (title, genre, release_year) VALUES ('Titanic', 'Drama/Romance', 1997);
INSERT INTO movie (title, genre, release_year) VALUES ('The Shawshank Redemption', 'Drama', 1994);
INSERT INTO movie (title, genre, release_year) VALUES ('Jurassic Park', 'Science Fiction/Adventure', 1993);
INSERT INTO movie (title, genre, release_year) VALUES ('The Matrix', 'Science Fiction/Action', 1999);
INSERT INTO movie (title, genre, release_year) VALUES ('Avatar', 'Science Fiction/Adventure', 2009);
INSERT INTO movie (title, genre, release_year) VALUES ('Forrest Gump', 'Drama/Romance', 1994);
INSERT INTO movie (title, genre, release_year) VALUES ('Star Wars: Episode IV - A New Hope', 'Science Fiction/Adventure', 1977);
INSERT INTO movie (title, genre, release_year) VALUES ('The Lord of the Rings: The Return of the King', 'Fantasy/Adventure', 2003);
INSERT INTO movie (title, genre, release_year) VALUES ('Hidden Figures', 'Drama', 2016);
```

## 5. Create the table

```bash
Rasianas-MacBook-Pro:~ rasianabrown$ psql -h 127.0.0.1 movie_directory

movie_directory=# SELECT * FROM movie;
 id |                     title                     |           genre           | release_year 
----+-----------------------------------------------+---------------------------+--------------
  1 | Titanic                                       | Drama/Romance             |         1997
  2 | The Shawshank Redemption                      | Drama                     |         1994
  3 | Jurassic Park                                 | Science Fiction/Adventure |         1993
  4 | The Matrix                                    | Science Fiction/Action    |         1999
  5 | Avatar                                        | Science Fiction/Adventure |         2009
  6 | Forrest Gump                                  | Drama/Romance             |         1994
  7 | Star Wars: Episode IV - A New Hope            | Science Fiction/Adventure |         1977
  8 | The Lord of the Rings: The Return of the King | Fantasy/Adventure         |         2003
  9 | Hidden Figures                                | Drama                     |         2016
(9 rows)

movie_directory=# 