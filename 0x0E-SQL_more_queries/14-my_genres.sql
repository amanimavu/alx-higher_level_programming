-- list all genres of the show Dexter
-- tv_show table contains only one record where title = Dexter
-- records should display: tv_genre.name
-- database name will be passed as an argument of the mysql cammand

    SELECT tv_genres.name
      FROM tv_show_genres
INNER JOIN (tv_shows, tv_genres)
        ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
     WHERE tv_shows.title = 'Dexter'
  ORDER BY tv_genres.name ASC;
