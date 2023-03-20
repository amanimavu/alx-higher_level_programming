-- list all records of the `second_table` from the current database
-- only the columns score and name should be included
-- records should be ordered in descending order of score

SELECT score, name FROM second_table
ORDER BY score DESC;
