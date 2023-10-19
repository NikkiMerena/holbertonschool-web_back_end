-- Create a temporary table to store the results
CREATE TEMPORARY TABLE IF NOT EXISTS temp_results AS (
    SELECT origin, SUM(nb_fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
);

-- Rank the country origins by the number of (non-unique) fans
SET @rank = 0;
SELECT origin, nb_fans, (@rank := @rank + 1) AS rank
FROM temp_results
ORDER BY nb_fans DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temp_results;
