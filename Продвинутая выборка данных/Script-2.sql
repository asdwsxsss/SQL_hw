#Название и продолжительность самого длительного трека.

SELECT name, duration FROM tracks 
ORDER BY duration DESC 
LIMIT 1;

#Название треков, продолжительность которых не менее 3,5 минут.

SELECT name, duration FROM tracks
WHERE duration > 3.5
GROUP BY name, duration;

#Названия сборников, вышедших в период с 2018 по 2020 год включительно.

SELECT name, year FROM collections
WHERE year BETWEEN 2018 AND 2020
GROUP BY name, year;

#Исполнители, чьё имя состоит из одного слова.

SELECT nickname FROM executors
WHERE nickname NOT LIKE '%% %%'

#Название треков, которые содержат слово «мой» или «my».

SELECT name FROM tracks
WHERE name  LIKE '%%my%%'

#Количество исполнителей в каждом жанре.

SELECT g.name, COUNT(e.executors_id) FROM executors e
JOIN executors_genres eg ON eg.executors_id = e.executors_id
JOIN genres g ON g.genre_id = eg.genre_id
GROUP BY g.name
ORDER BY g.name
 
#Количество треков, вошедших в альбомы 2019–2020 годов.

SELECT a.year_of_release, COUNT(t.track_id) FROM tracks t
JOIN albums a ON a.album_id = t.album_id
WHERE a.year_of_release IN (2019, 2020)
GROUP BY a.year_of_release
 
#Средняя продолжительность треков по каждому альбому.

SELECT a.name, AVG(t.duration) AS average_track_duration FROM tracks t
JOIN albums a ON a.album_id = t.album_id
GROUP BY a.name
ORDER BY a.name
 
#Все исполнители, которые не выпустили альбомы в 2020 году.

SELECT e.nickname  FROM executors e
JOIN executors_albums ea ON ea.executors_id  = e.executors_id
JOIN albums a ON a.album_id = ea.album_id
WHERE e.nickname NOT IN (SELECT e.nickname FROM executors e
              				JOIN executors_albums ea ON ea.executors_id = e.executors_id
              				JOIN albums a ON a.album_id = ea.album_id 
              				WHERE a.year_of_release = 2020)
ORDER BY e.nickname
 
#Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).

SELECT c.name FROM collections c 
JOIN collections_tracks ct ON ct.collection_id  = c.collection_id
JOIN tracks t ON t.track_id  = ct.track_id
JOIN albums a ON a.album_id = t.album_id
JOIN executors_albums ea ON ea.album_id = a.album_id 
JOIN executors e ON e.executors_id  = ea.executors_id 
WHERE e.nickname  = 'Imagine Dragons' 
ORDER BY c.name
