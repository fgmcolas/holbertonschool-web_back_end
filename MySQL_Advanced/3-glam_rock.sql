-- Task: 3. Old school band - inserts rows into the `users` table with the `age` column set to a value under 21
-- Script can be executed on any database
SELECT DISTINCT `band_name`,
                IFNULL(`split`, 2020) - `formed` as `lifespan`
    FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style)
    ORDER BY `lifespan` DESC;
