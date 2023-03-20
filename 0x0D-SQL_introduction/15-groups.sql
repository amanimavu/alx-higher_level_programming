-- list the number of records with the same score from a given table
-- result should display score and number of records for the score
-- sort the result by the number of records

SELECT score, COUNT(*) AS `number` FROM second_table
GROUP BY score
ORDER BY `number` DESC
