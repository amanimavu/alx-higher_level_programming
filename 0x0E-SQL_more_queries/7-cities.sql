-- create a database hbtn_0d_usa if it alredy exits the script shouldn't fail
-- create the table cities (in the database hbtn_0d_usa), script shouldn't fail if it already exists
-- id column should hold values that are integers, not null and primary keys
-- state_id column should hold values that are integers, not null and foreign keys
-- name column should hold values that are VARCHAR and not null

  CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
     USE hbtn_0d_usa;
  CREATE TABLE IF NOT EXISTS cities(
      id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
	 FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL)
	 ENGINE=InnoDB;
