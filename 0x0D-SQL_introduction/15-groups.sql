-- lists number of records with same value
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score;

