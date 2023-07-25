-- list cities in a state
-- based o our database

SELECT id, name FROM cities
WHERE state_id = (select id from states where name = "california")
ORDER BY id DESC;
