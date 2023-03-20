-- list all records with score >= 10 of the `second_table` from the current database
-- results should be displayed in descending order of score
-- only the columns score and name should be displayed

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
