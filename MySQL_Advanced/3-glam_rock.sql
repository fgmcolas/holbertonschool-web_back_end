-- Task: 3. Old school bandlists - all bands with Glam as their main style
-- Script can be executed on any database
SELECT name AS band_name, IFNULL(YEAR(COALESCE(split, CURDATE())) - YEAR(formed), 0) AS lifespan
FROM metal_bands WHERE style = 'Glam rock' ORDER BY lifespan DESC;
