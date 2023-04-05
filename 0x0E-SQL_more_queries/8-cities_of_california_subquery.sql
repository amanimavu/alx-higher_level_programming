-- lists all cities of Carlifornia that can be found in the database hbtn_0d_usa
-- result must be assorted in ascending order by cities.id
-- database name will be passed as an argument of the mysql command

SELECT * FROM cities
 WHERE state_id = (
       SELECT id FROM states
       WHERE name = 'California');
