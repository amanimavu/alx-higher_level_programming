-- lists all cities contained in the database hbtn_0d_usa
-- each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- database name will be passed as argument of the mysql command

   SELECT cities.id, cities.name, states.name
     FROM cities
LEFT JOIN states
       ON states.id = cities.state_id
 ORDER BY cities.id ASC
