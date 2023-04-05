-- list all shows contained that have atleast  one genre
-- records should be displayed in ascending order by tv_shows.title and tv_show_genre.genre_id
-- database name will be passed as an argument of the mysql command

    SELECT tv_shows.title, tv_show_genres.genre_id
      FROM tv_shows
INNER JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
