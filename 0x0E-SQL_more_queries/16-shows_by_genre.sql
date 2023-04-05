-- list all shows, and all genre linked to that show, from the databse hbtn_0d_tvshows
-- if a show doesn't have a genre, display NULL in the genre column
-- records should display: tv_shows.title - tv_genres.name
-- results must be sorted in ascending order by the show title and genre name
-- database name will be passed as argumnent of the mysql command

   SELECT tv_shows.title, tv_genres.name
     FROM tv_shows
LEFT JOIN (tv_genres, tv_show_genres)
       ON (tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id)
 ORDER BY tv_shows.title, tv_genres.name ASC;
