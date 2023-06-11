CREATE TABLE IF NOT EXISTS genres(
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS executors(
	executors_id SERIAL PRIMARY KEY, 
	nickname VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS executors_genres(
	genre_id  INTEGER NOT NULL REFERENCES genres(genre_id),
	executors_id INTEGER NOT NULL REFERENCES executors(executors_id),
	PRIMARY KEY (genre_id, executors_id)
);

CREATE TABLE IF NOT EXISTS albums(
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	year_of_release INTEGER CHECK (year_of_release > 0)
);

CREATE TABLE IF NOT EXISTS executors_albums(
	executors_id INTEGER REFERENCES executors(executors_id),
	album_id  INTEGER REFERENCES albums(album_id),
	PRIMARY KEY (executors_id, album_id)
);

CREATE TABLE IF NOT EXISTS tracks(
	track_id SERIAL PRIMARY KEY,
	album_id INTEGER REFERENCES albums(album_id),
	name VARCHAR(60) NOT NULL,
	duration time NOT NULL CHECK  (duration < '10:00:00')
);

CREATE TABLE IF NOT EXISTS collections(
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	year INTEGER CHECK (year > 0)
);

CREATE TABLE IF NOT EXISTS collections_tracks(
	track_id INTEGER REFERENCES tracks(track_id),
	collection_id INTEGER REFERENCES collections(collection_id),
	PRIMARY KEY (track_id, collection_id)
);