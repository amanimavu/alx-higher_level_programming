-- list all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- record should display: <TV show genre> - <NUmber of shows linked to this genre>
-- second column must be called number_of_shows
-- don't display genre that doesn't have any shows linked
-- results must be sorted in ascending order by the number of shows linked
-- database name will be passed as an argument of the mysql command

	SELECT tv_genres.name, COUNT(*) AS number_of_shows
	  FROM tv_genres
    INNER JOIN tv_show_genres
            ON tv_genres.id = tv_show_genres.genre_id
      GROUP BY tv_genres.name
      ORDER BY number_of_shows DESC;
