-- Task: 2. Best band ever! - inserts a row into the `users` table
-- Script can be executed on any database
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
