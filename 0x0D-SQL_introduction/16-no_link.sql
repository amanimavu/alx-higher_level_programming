-- list all records of tha table `second_table`
-- don't list rows without a name value
-- results should display the score and name (in this order)
-- have the records ordered by score

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
