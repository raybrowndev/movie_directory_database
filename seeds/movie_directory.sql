-- Then, we recreate them
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS movie;
DROP SEQUENCE IF EXISTS movie_id_seq;

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
