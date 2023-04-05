-- list all shows contained inhbtn_od_tvshows without genre
-- results must be sorted in ascending order b tv_shows.title and tv_show_genres.genre_id
-- database name will be passed as argument of the mysql command

         SELECT tv_shows.title, tv_show_genres.genre_id
           FROM tv_shows
      LEFT JOIN tv_show_genres
             ON tv_shows.id = tv_show_genres.show_id
	  WHERE tv_show_genres.show_id IS NULL
       ORDER BY tv_shows.title, tv_show_genres.genre_id;
