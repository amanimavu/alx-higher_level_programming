-- create MYSQL server user user_0d_1
-- password for user_0d_1 should be set to user_0d_1_pwd
-- script should not fail if the user user_0d_1 already exists

CREATE USER IF NOT EXISTS'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
 GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
