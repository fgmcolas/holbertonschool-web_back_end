-- Task: 2. Best band ever! - inserts a row into the `users` table with specific values for `name`, `email`, and `age`
-- Script can be executed on any database
SELECT origin, SUM("fans") AS "nb_fans"
FROM metal_bands
GROUP BY "origin"
ORDER BY "nb_fans" DESC;