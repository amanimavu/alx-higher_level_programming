-- create the table id_not_null
-- id_not_null should have columns: id(INT), name(VARCHAR[256])
-- database name will be passed as an argument of the mysql command
-- if id_not_null already exists, your script shouldn't fail

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
  name VARCHAR(256))
