-- create a table force_name
-- force_name has columns id(INT) and name(VARCHAR[256])
-- database name will be passed as an argument of mysql command
-- if force_name already exists, script should not fail

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
  name VARCHAR(256))
