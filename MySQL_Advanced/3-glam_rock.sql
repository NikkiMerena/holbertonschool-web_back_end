-- Task 3 List all bands with Glam Rock as main style
-- Ranked by longeivity
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
