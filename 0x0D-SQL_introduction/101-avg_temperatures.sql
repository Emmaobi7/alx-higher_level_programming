-- displays average temperature from imported data
-- ordr by descending temprature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

