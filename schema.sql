CREATE TABLE users (
  id TEXT PRIMARY KEY,
  name TEXT,
  email TEXT,
  profile_image_url TEXT
);

CREATE TABLE images (
  id SERIAL PRIMARY KEY,
  name TEXT,
  data BYTEA
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  created_at TIMESTAMP,
  lat DOUBLE PRECISION,
  long DOUBLE PRECISION,
  image INTEGER REFERENCES images (id),
  creator TEXT REFERENCES users (id),
  teksti TEXT 
);

CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  tag TEXT
);

CREATE TABLE posts_to_tags (
  post_id INTEGER REFERENCES posts (id),
  tag_id INTEGER REFERENCES tags (id)
);