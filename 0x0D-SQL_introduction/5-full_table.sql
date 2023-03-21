-- print full description of table `first_table`
-- no using DESCRIBE or EXPLAIN

SELECT * FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0'
AND TABLE_NAME = 'first_table';
