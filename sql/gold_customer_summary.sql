-- Customer count per postcode area for the reporting layer
SELECT
    LEFT(postcode, 2) AS postcode_area,
    COUNT(*)          AS customers
FROM silver_customers
GROUP BY LEFT(postcode, 2)
ORDER BY customers DESC;
