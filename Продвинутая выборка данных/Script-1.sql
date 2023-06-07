ALTER TABLE albums
ALTER COLUMN year_of_release TYPE INTEGER USING year_of_release::INTEGER

ALTER TABLE collections 
ALTER COLUMN year TYPE INTEGER USING year::INTEGER

INSERT INTO executors
VALUES (1, 'Rihanna'), (2, 'Imagine Dragons'), (3, 'The Weeknd'), (4, 'Tanir')

INSERT INTO genres 
VALUES (1, 'Hip-hop'), (2, 'Rock'), (3, 'Popular music')

INSERT INTO albums  
VALUES (1, 'Unapologetic', 2012), (2, 'Mercury-Act 1', 2021), (3, 'Starboy', 2016)

INSERT INTO tracks  
VALUES (1, 3, 'True Colors', 3.26), (2,2, 'Lonely', 2.36), (3,2, 'Enemy', 4.3), (4, 1, 'Diamonds', 2.21), (5,1, 'Stay', 3.12), (6,1, 'Numb', 3.42)

INSERT INTO collections  
VALUES (1, 'col-1', 2017), (2, 'col-2', 2023), (3, 'col-3', 2022), (4, 'col-4', 2018)

INSERT INTO collections_tracks  
VALUES (3, 1), (5, 4)

INSERT INTO executors_albums  
VALUES (1, 1), (2, 2), (3,3)

INSERT INTO executors_genres  
VALUES (3, 1), (1, 3)