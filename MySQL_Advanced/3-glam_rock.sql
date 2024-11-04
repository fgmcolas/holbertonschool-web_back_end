SELECT band_name,
IFNULL(YEAR(split) - YEAR(formed), 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
