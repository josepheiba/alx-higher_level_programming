-- show grants
SELECT cities.id, cities.name FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';
