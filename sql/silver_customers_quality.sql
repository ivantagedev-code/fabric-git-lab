-- Rows in silver_customers with a missing or malformed postcode
SELECT customer_id, customer_name, postcode
FROM silver_customers
WHERE postcode IS NULL
   OR LEN(postcode) < 5;
