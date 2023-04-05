-- script that lists all Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy (but id can be different)
-- results must be sorted in ascending order by the show title
-- databse will be passed as an argument to mysql command

    SELECT tv_shows.title
      FROM tv_show_genres
INNER JOIN (tv_shows, tv_genres)
        ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
     WHERE tv_genres.name = 'Comedy'
  ORDER BY tv_shows.title;
