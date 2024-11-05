-- Task: 3. Old school band - inserts rows into the `users` table with the `age` column set to a value under 21
-- Script can be executed on any database
SELECT band_name,
IFNULL(YEAR(split) - YEAR(formed), 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
