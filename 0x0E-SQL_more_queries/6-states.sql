-- create a database hbtn_0d_1 and table states(in the database hbtn_0d_usa)
-- state should have columns: id(INT) unique and auto generated and name(VARCHAR[256])
-- if databse hbtn_0d_usa already exists, script shouldn't fail
-- if table states already exists, script shou;dn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT,
  name VARCHAR(256) NOT NULL)
