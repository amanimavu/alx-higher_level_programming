-- create the table unique_id
-- unique_id should contain columns: id(INT) and name(VARCHAR[256])
-- column id should be unique
-- if table already exists, script should not fail
-- databse name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256))
