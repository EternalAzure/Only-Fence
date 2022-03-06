DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS images CASCADE;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    text TEXT
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    posts_id INTEGER 
    REFERENCES posts
    ON DELETE CASCADE,
    data BYTEA
);