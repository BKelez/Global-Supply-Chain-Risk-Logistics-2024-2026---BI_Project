SELECT
    c.product_category,
    AVG(f.lead_time_days) AS avg_lead_time
FROM fact_shipments f
JOIN dim_product_category c
ON f.product_category_id = c.product_category_id
GROUP BY c.product_category
ORDER BY avg_lead_time DESC;