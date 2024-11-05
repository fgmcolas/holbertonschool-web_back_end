-- Task: 3. Old school bandlists - all bands with Glam as their main style
-- Script can be executed on any database
SELECT band_name, COALESCE(split, 2024) - formed AS lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
